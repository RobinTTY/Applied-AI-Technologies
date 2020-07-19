from __future__ import division
from __future__ import print_function

from PIL import Image
from PostIt import PostIt
import numpy as np
import cv2 as cv


class ImagePreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.img = cv.imread(file_path, 1)
        self.post_its = []

    @staticmethod
    def convert_image(file_path):
        """convert image to right dimensions"""
        img = Image.open(file_path)
        img = img.convert("L")
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
        img.show()
        img = img.resize((128, int(img.size[1] * (128 / img.size[0]))))

        if img.size[1] > 32:
            img = img.resize((int(img.size[0] * (32 / img.size[1])), 32))

        bg = Image.new('RGBA', (128, 32), (255, 255, 255, 255))
        bg.paste(img, (0, 0))
        return bg

    @staticmethod
    def preprocess(img, img_size, data_augmentation=False):
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

    def pre_preprocess(self, resize_factor):
        lab = cv.cvtColor(self.img, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(lab)
        enhanced = cv.createCLAHE(clipLimit=2.0, tileGridSize=(1, 1))
        cl = enhanced.apply(l)
        merged = cv.merge((cl, a, b))
        final_rgb = cv.cvtColor(merged, cv.COLOR_LAB2BGR)
        final_gray = cv.cvtColor(final_rgb, cv.COLOR_RGB2GRAY)
        self.img = cv.resize(final_gray, (0, 0), fx=(1 / resize_factor), fy=(1 / resize_factor))

    def find_post_its(self, resize_factor=2):
        img = Image.open(self.file_path)
        arr = np.array(img)

        y_dim = arr.shape[0]
        x_dim = arr.shape[1]
        test_arr = np.zeros((y_dim, x_dim))

        for y in range(y_dim):
            for x in range(x_dim):
                r, g, b = arr[y][x]

                if max(r, g, b) - min(r, g, b) < 20:
                    test_arr[y][x] = 255

        test_img = Image.fromarray(test_arr)
        test_img = test_img.convert('RGB')
        test_img.save("../data/black_white.png")
        self.img = cv.imread("../data/black_white.png")

        self.pre_preprocess(resize_factor)
        _, threshold = cv.threshold(self.img, 240, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        file = Image.open(self.file_path)
        width, height = file.size
        count = 0

        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if ((width * height) / 999) < (w * h) < ((width * height) / 10):
                x, y, w, h = (x * resize_factor, y * resize_factor, w * resize_factor, h * resize_factor)
                out = file.crop((x, y, x + w, y + h))
                out_path = f"../data/output_{count}.png"
                self.post_its.append(PostIt(out_path, (x, y, w, h)))
                out.save(out_path)
                count = count + 1

    def print_info(self):
        for x in range(len(self.post_its)):
            self.post_its[x].print_info()
            print()

    # not used atm
    def find_words(self):
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
