import tensorflow as tf
from ImagePreprocessor import ImagePreprocessor
from Batch import Batch
from Model import Model, DecoderType
import os
import sys


class PostItExtractor:
    def __init__(self, debug_mode=False):
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        tf.compat.v1.disable_eager_execution()
        self.decoder_type = DecoderType.BestPath
        self.model = Model(open('../model/charList.txt').read(), self.decoder_type, must_restore=True)
        self.debug_mode = debug_mode

    def image_to_post_its(self, image=""):
        file_path = "../data/colored/MultiplePostIts6.jpg"
        pre_processor = ImagePreprocessor(self.debug_mode)
        post_its = pre_processor.find_post_its(file_path)

        for post_it in post_its:
            img = pre_processor.convert_image(post_it.file)
            post_it.file = img
            post_it.text = self.extract_text(self.model, post_it.file)
            print(post_it)

        return post_its

    @staticmethod
    def extract_text(model, input_img):
        """recognize text in image provided by file path"""
        img = ImagePreprocessor.preprocess(input_img, Model.imgSize)
        batch = Batch(None, [img])
        (recognized, probability) = model.infer_batch(batch, True)
        return recognized[0]


def main():
    extractor = PostItExtractor(debug_mode=False)
    try:
        extractor.image_to_post_its()
    except Exception as exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, file_name, exc_tb.tb_lineno)
        print(exception)


if __name__ == '__main__':
    main()
