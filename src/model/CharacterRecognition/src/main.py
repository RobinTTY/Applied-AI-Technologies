from __future__ import division
from __future__ import print_function

import cv2
import tensorflow as tf
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
    #print('Recognized:', '"' + recognized[0] + '"')
    #print('Probability:', probability[0])
    return recognized[0]


def main():
    # TODO: check if needed
    tf.compat.v1.disable_eager_execution()
    decoder_type = DecoderType.BestPath

    # preprocess images
    file_path = "../data/colored/MultiplePostIts.png"
    obj = ImagePrePreprocessor(file_path)
    obj.find_post_its()

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
