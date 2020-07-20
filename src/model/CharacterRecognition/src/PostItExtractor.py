import cv2
import tensorflow as tf
from ImagePreprocessor import ImagePreprocessor
from Batch import Batch
from Model import Model, DecoderType
import os


class PostItExtractor:
    def __init__(self, debug_mode=False):
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        tf.compat.v1.disable_eager_execution()
        self.decoder_type = DecoderType.BestPath
        self.model = Model(open('../model/charList.txt').read(), self.decoder_type, must_restore=True)
        self.debug_mode = debug_mode

    def process_image(self):
        file_path = "../data/colored/MultiplePostIts5.jpg"
        pre_processor = ImagePreprocessor(file_path, self.debug_mode)
        post_its = pre_processor.find_post_its()

        for post_it in post_its:
            img = pre_processor.convert_image(post_it.file)
            post_it.file = img
            post_it.text = self.extract_text(self.model, post_it.file)
            print(post_it)

    @staticmethod
    def extract_text(model, input_img):
        """recognize text in image provided by file path"""
        img = ImagePreprocessor.preprocess(input_img, Model.imgSize)
        batch = Batch(None, [img])
        (recognized, probability) = model.infer_batch(batch, True)
        return recognized[0]


def main():
    extractor = PostItExtractor(debug_mode=False)
    extractor.process_image()


if __name__ == '__main__':
    main()
