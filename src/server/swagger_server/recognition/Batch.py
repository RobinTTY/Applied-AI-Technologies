import numpy as np


class Batch:
    """batch containing images and ground truth texts"""

    def __init__(self, gt_texts, images):
        self.images = np.stack(images, axis=0)
        self.gtTexts = gt_texts