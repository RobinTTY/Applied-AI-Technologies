import cv2
import tensorflow as tf
from ImagePreprocessor import ImagePreprocessor
from Batch import Batch
from Model import Model, DecoderType


class PostItExtractor:
    def __init__(self, debug_mode=False):
        tf.compat.v1.disable_eager_execution()
        self.decoder_type = DecoderType.BestPath
        self.model = Model(open('../model/charList.txt').read(), self.decoder_type, must_restore=True)
        self.debugMode = debug_mode

    def process_image(self, image):
        # TODO: pass image properly

        # preprocess images
        file_path = "../data/colored/MultiplePostIts.jpg"
        pre_processor = ImagePreprocessor(file_path)
        pre_processor.find_post_its()

        for x in range(len(pre_processor.post_its)):
            img = ImagePreprocessor.convert_image(pre_processor.post_its[x].file_path)
            img.save(f"../data/output_{x}.png")

        for x in range(len(pre_processor.post_its)):
            pre_processor.post_its[x].text = self.extract_text(self.model, pre_processor.post_its[x].file_path)

        pre_processor.print_info()

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
    extractor = PostItExtractor(debug_mode=False)
    extractor.process_image(123)


if __name__ == '__main__':
    main()
