from __future__ import division
from __future__ import print_function

from PIL import Image
import numpy as np
import cv2


class ImagePreprocessor:
    @staticmethod
    def convert_image(file_path):
        img = Image.open(file_path)
        img = img.convert("L").resize((128, int(img.size[1] * (128 / img.size[0]))))

        if img.size[1] > 32:
            img = img.resize((int(img.size[0] * (32 / img.size[1])), 32))

        average = np.average(np.array(img))
        img = Image.fromarray(np.where(np.array(img) > 0.9 * average, 255, 0))
        bg = Image.new('RGBA', (128, 32), (255, 255, 255, 255))
        bg.paste(img, (0, 0))
        return bg

    @staticmethod
    def preprocess(img, img_size, data_augmentation=False):
        """put img into target img of size imgSize, transpose for TF and normalize gray-values"""

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
        img = cv2.resize(img, new_size)
        target = np.ones([ht, wt]) * 255
        target[0:new_size[1], 0:new_size[0]] = img

        # transpose for TF
        img = cv2.transpose(target)

        # normalize
        (m, s) = cv2.meanStdDev(img)
        m = m[0][0]
        s = s[0][0]
        img = img - m
        img = img / s if s > 0 else img
        return img
