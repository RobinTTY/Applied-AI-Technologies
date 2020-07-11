from __future__ import division
from __future__ import print_function

import cv2
import tensorflow as tf
from ImagePrePreprocessor import ImagePrePreprocessor
from ImagePreprocessor import ImagePreprocessor
from DataLoader import Batch
from Model import Model, DecoderType


class FilePaths:
    """relevant file paths"""
    fnCharList = '../model/charList.txt'
    fnAccuracy = '../model/accuracy.txt'
    fnInfer = '../data/output.png'


class PostItExtractor:
    def __init__(self):
        tf.compat.v1.disable_eager_execution()
        self.decoder_type = DecoderType.BestPath
        self.model = Model(open(FilePaths.fnCharList).read(), self.decoder_type, must_restore=True)

    def process_image(self, image):
        # TODO: pass image properly

        # preprocess images
        file_path = "../data/colored/MultiplePostIts3.png"
        obj = ImagePrePreprocessor(file_path)
        obj.find_post_its()

        for x in range(len(obj.post_its)):
            img = ImagePreprocessor.convert_image(obj.post_its[x].file_path)
            img.save(f"../data/output_{x}.png")

        # infer text on test image
        print(open(FilePaths.fnAccuracy).read())

        for x in range(len(obj.post_its)):
            obj.post_its[x].text = self.extract_text(self.model, obj.post_its[x].file_path)

        obj.print_info()

    @staticmethod
    def extract_text(model, input_img):
        """recognize text in image provided by file path"""
        img = ImagePreprocessor.preprocess(cv2.imread(input_img, cv2.IMREAD_GRAYSCALE), Model.imgSize)
        batch = Batch(None, [img])
        (recognized, probability) = model.infer_batch(batch, True)
        print('Recognized:', '"' + recognized[0] + '"')
        print('Probability:', probability[0])
        return recognized[0]


def main():
    extractor = PostItExtractor()
    extractor.process_image(123)


if __name__ == '__main__':
    main()
