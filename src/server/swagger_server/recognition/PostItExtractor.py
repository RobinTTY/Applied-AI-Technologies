import tensorflow as tf
from .ImagePreprocessor import ImagePreprocessor
from .Batch import Batch
from .Model import Model
from .PostItGroup import PostItGroup
import os
import sys


def main():
    """for testing purposes"""
    extractor = PostItExtractor(debug_mode=False)
    try:
        post_its = extractor.image_to_post_its("../test_data/colored/MultiplePostIts8.jpg")
        post_it_groups = extractor.group_post_its(post_its)

        for group in post_it_groups:
            print(group)

    except Exception as exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, file_name, exc_tb.tb_lineno)
        print(exception)


class PostItExtractor:
    def __init__(self, debug_mode=False):
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        tf.compat.v1.disable_eager_execution()
        self.model = Model(must_restore=True)
        self.debug_mode = debug_mode

    def image_to_post_its(self, image):
        pre_processor = ImagePreprocessor(self.debug_mode)
        post_its = pre_processor.find_post_its(image)

        for post_it in post_its:
            img = pre_processor.convert_image(post_it.file)
            post_it.file = img
            post_it.text = self.extract_text(self.model, post_it.file)
            post_it.rgb = pre_processor.get_color(image, post_it.rect)

        return post_its

    @staticmethod
    def group_post_its(ungrouped_post_its):
        """groups post-its by color, adjacent colors get grouped together"""
        groups = []

        for post_it in ungrouped_post_its:
            found_group = False

            for group in groups:
                diff = (
                    abs(post_it.rgb[0] - group.color[0]),
                    abs(post_it.rgb[1] - group.color[1]),
                    abs(post_it.rgb[2] - group.color[2])
                )

                if max(diff[0], diff[1], diff[2]) < 30:
                    group.post_its.append(post_it)
                    post_it.color_grp = group.color
                    found_group = True

            if not found_group:
                grp = PostItGroup(post_it.rgb)
                post_it.color_grp = post_it.rgb
                grp.post_its.append(post_it)
                groups.append(grp)

        return groups

    @staticmethod
    def extract_text(model, input_img):
        """recognize text in image provided by file path"""
        img = ImagePreprocessor.preprocess(input_img, Model.imgSize)
        batch = Batch(None, [img])
        (recognized, probability) = model.infer_batch(batch, True)
        return recognized[0]


if __name__ == '__main__':
    main()