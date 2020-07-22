from __future__ import division
from __future__ import print_function

from PIL import Image
from .PostItInternal import PostItInternal
import numpy as np
import cv2 as cv
import time


class ImagePreprocessor:
    def __init__(self, debug_mode):
        self.debug_mode = debug_mode

    def convert_image(self, file):
        """convert image to right dimensions"""
        img = file.convert("L")
        average = np.average(np.array(img))
        img = Image.fromarray(np.where(np.array(img) > 0.4 * average, 255, 0))

        max_x = max_y = 0
        min_x = min_y = 1000000
        img_arr = np.array(img)

        for x in range(img_arr.shape[0]):
            for y in range(img_arr.shape[1]):
                if img_arr[x][y] == 0:
                    min_x = x if x < min_x else min_x
                    min_y = y if y < min_y else min_y
                    max_x = x if x > max_x else max_x
                    max_y = y if y > max_y else max_y

        img = img.crop((min_y - 2, min_x - 2, max_y + 2, max_x + 2))

        if self.debug_mode:
            img.show()

        img = img.resize((128, int(img.size[1] * (128 / img.size[0]))))

        if img.size[1] > 32:
            img = img.resize((int(img.size[0] * (32 / img.size[1])), 32))

        bg = Image.new('RGBA', (128, 32), (255, 255, 255, 255))
        bg.paste(img, (0, 0))
        imcv = cv.cvtColor(np.asarray(bg), cv.COLOR_RGB2GRAY)
        return imcv

    @staticmethod
    def get_color(image, rect):
        img = image.crop((rect[0], rect[1], rect[0] + rect[2], rect[1] + rect[3]))

        r = img.getchannel('R')
        g = img.getchannel('G')
        b = img.getchannel('B')

        r_avg = int(np.average(np.array(r)))
        g_avg = int(np.average(np.array(g)))
        b_avg = int(np.average(np.array(b)))

        return r_avg, g_avg, b_avg

    @staticmethod
    def preprocess(img, img_size):
        """default image transformations"""

        # there are damaged files in IAM dataset - just use black image instead
        if img is None:
            print("Image is None!")
            img = np.zeros([img_size[1], img_size[0]])

        # create target image and copy sample image into it
        (wt, ht) = img_size
        (h, w) = img.shape
        fx = w / wt
        fy = h / ht
        f = max(fx, fy)
        # scale according to f (result at least 1 and at most wt or ht)
        new_size = (max(min(wt, int(w / f)), 1), max(min(ht, int(h / f)), 1))
        img = cv.resize(img, new_size)
        target = np.ones([ht, wt]) * 255
        target[0:new_size[1], 0:new_size[0]] = img

        # transpose for TF
        img = cv.transpose(target)

        # normalize
        (m, s) = cv.meanStdDev(img)
        m = m[0][0]
        s = s[0][0]
        img = img - m
        img = img / s if s > 0 else img
        return img

    @staticmethod
    def resize(image, resize_factor):
        lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(lab)
        enhanced = cv.createCLAHE(clipLimit=2.0, tileGridSize=(1, 1))
        cl = enhanced.apply(l)
        merged = cv.merge((cl, a, b))
        final_rgb = cv.cvtColor(merged, cv.COLOR_LAB2BGR)
        final_gray = cv.cvtColor(final_rgb, cv.COLOR_RGB2GRAY)
        return cv.resize(final_gray, (0, 0), fx=(1 / resize_factor), fy=(1 / resize_factor))

    def find_post_its(self, image_input, resize_factor=2):
        """returns number of detected post-it's"""
        arr = np.array(image_input)

        y_dim = arr.shape[0]
        x_dim = arr.shape[1]
        test_arr = np.zeros((y_dim, x_dim))

        # this loop takes supaaaaa long
        start = time.time()
        for y in range(y_dim):
            for x in range(x_dim):
                r, g, b = arr[y][x]

                if max(r, g, b) - min(r, g, b) < 20:
                    test_arr[y][x] = 255
        end = time.time()
        print(f"find post it loop: {end - start}")

        test_img = Image.fromarray(test_arr)
        test_img = test_img.convert('RGB')
        image = cv.cvtColor(np.asarray(test_img), cv.COLOR_RGB2BGR)

        image = self.resize(image, resize_factor)
        _, threshold = cv.threshold(image, 240, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        width, height = image_input.size
        count = 0

        post_its = []
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if ((width * height) / 999) < (w * h) < ((width * height) / 10):
                x, y, w, h = (x * resize_factor, y * resize_factor, w * resize_factor, h * resize_factor)
                post_it_file = image_input.crop((x, y, x + w, y + h))
                post_it = PostItInternal(post_it_file, (x, y, w, h))
                post_its.append(post_it)
                count += 1

        return post_its

    # not used atm
    @staticmethod
    def find_words():
        img = cv.imread('../data/input2.jpg', 0)
        cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU, img)

        contours, image = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        for c in contours:
            # get the bounding rect
            x, y, w, h = cv.boundingRect(c)
            # draw a white rectangle to visualize the bounding rect
            cv.rectangle(img, (x, y), (x + w, y + h), 255, 1)

        cv.drawContours(img, contours, -1, (255, 255, 0), 1)

        cv.imwrite("../data/output.png", img)
