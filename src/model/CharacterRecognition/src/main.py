from __future__ import division
from __future__ import print_function

import os
import cv2
import tensorflow as tf
from WordSegmentation import segment_word, prepare_img
from ImagePrePreprocessor import ImagePrePreprocessor
from ImagePreprocessor import ImagePreprocessor
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType


class FilePaths:
    """relevant file paths"""
    fnCharList = '../model/charList.txt'
    fnAccuracy = '../model/accuracy.txt'
    fnInfer = '../data/output.png'


def extract_text(model, input_img):
    """recognize text in image provided by file path"""
    img = ImagePreprocessor.preprocess(cv2.imread(input_img, cv2.IMREAD_GRAYSCALE), Model.imgSize)
    batch = Batch(None, [img])
    (recognized, probability) = model.infer_batch(batch, True)
    return recognized[0]


def test_word_segmentation():
    """reads images from data/ and outputs the word-segmentation to out/"""

    # read input images from 'in' directory
    imgFiles = os.listdir('../seg/data/')
    for (i, f) in enumerate(imgFiles):
        print('Segmenting words of sample %s' % f)

        # read image, prepare it by resizing it to fixed height and converting it to grayscale
        img = prepare_img(cv2.imread('../seg/data/%s' % f), 50)

        # execute segmentation with given parameters
        # -kernelSize: size of filter kernel (odd integer)
        # -sigma: standard deviation of Gaussian function used for filter kernel
        # -theta: approximated width/height ratio of words, filter function is distorted by this factor
        # - minArea: ignore word candidates smaller than specified area
        res = segment_word(img, kernel_size=25, sigma=2, theta=5, min_area=100)

        # write output to 'out/inputFileName' directory
        if not os.path.exists('../seg/out/%s' % f):
            os.mkdir('../seg/out/%s' % f)

        # iterate over all segmented words
        print('Segmented into %d words' % len(res))
        for (j, w) in enumerate(res):
            (wordBox, wordImg) = w
            (x, y, w, h) = wordBox
            # save word
            cv2.imwrite('../seg/out/%s/%d.png' % (f, j), wordImg)
            # draw bounding box in summary image
            cv2.rectangle(img, (x, y), (x + w, y + h), 0, 1)

        # output summary image with bounding boxes around words
        cv2.imwrite('../seg/out/%s/summary.png' % f, img)


def main():
    # TODO: check if needed
    tf.compat.v1.disable_eager_execution()
    decoder_type = DecoderType.BestPath

    # preprocess images
    file_path = "../data/colored/MultiplePostIts2.png"
    obj = ImagePrePreprocessor(file_path)
    num = obj.find_post_its()
    print(f"Found: {num}")

    for x in range(len(obj.post_its)):
        img = ImagePreprocessor.convert_image(obj.post_its[x].file_path)
        img.save(f"../data/output_{x}.png")

    # infer text on test image
    print(open(FilePaths.fnAccuracy).read())
    model = Model(open(FilePaths.fnCharList).read(), decoder_type, must_restore=True)

    for x in range(len(obj.post_its)):
        obj.post_its[x].text = extract_text(model, obj.post_its[x].file_path)

    obj.print_info()


if __name__ == '__main__':
    main()
