from __future__ import division
from __future__ import print_function

import sys
import math
import pickle
import copy
import numpy as np
import cv2
import matplotlib.pyplot as plt
from DataLoader import Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess


# constants like filepaths
class Constants:
    """filenames and paths to data"""
    fnCharList = '../model/charList.txt'
    fnAnalyze = '../data/analyze.png'
    fnPixelRelevance = '../data/pixelRelevance.npy'
    fnTranslationInvariance = '../data/translationInvariance.npy'
    fnTranslationInvarianceTexts = '../data/translationInvarianceTexts.pickle'
    gtText = 'are'
    distribution = 'histogram'  # 'histogram' or 'uniform'


def odds(val):
    return val / (1 - val)


def weight_of_evidence(orig_prob, marg_prob):
    return math.log2(odds(orig_prob)) - math.log2(odds(marg_prob))


def analyze_pixel_relevance():
    """simplified implementation of paper: Zintgraf et al - Visualizing Deep Neural Network Decisions: Prediction
    Difference Analysis """

    # setup model
    model = Model(open(Constants.fnCharList).read(), DecoderType.BestPath, mustRestore=True)

    # read image and specify ground-truth text
    img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
    (w, h) = img.shape
    assert Model.imgSize[1] == w

    # compute probability of gt text in original image
    batch = Batch([Constants.gtText], [preprocess(img, Model.imgSize)])
    (_, probs) = model.infer_batch(batch, calc_probability=True, probability_of_gt=True)
    orig_prob = probs[0]

    gray_values = [0, 63, 127, 191, 255]
    if Constants.distribution == 'histogram':
        bins = [0, 31, 95, 159, 223, 255]
        (hist, _) = np.histogram(img, bins=bins)
        pixel_prob = hist / sum(hist)
    elif Constants.distribution == 'uniform':
        pixel_prob = [1.0 / len(gray_values) for _ in gray_values]
    else:
        raise Exception('unknown value for Constants.distribution')

    # iterate over all pixels in image
    pixel_relevance = np.zeros(img.shape, np.float32)
    for x in range(w):
        for y in range(h):

            # try a subset of possible grayvalues of pixel (x,y)
            images_marginalized = []
            for g in gray_values:
                image_changed = copy.deepcopy(img)
                image_changed[x, y] = g
                images_marginalized.append(preprocess(image_changed, Model.imgSize))

            # put them all into one batch
            batch = Batch([Constants.gtText] * len(images_marginalized), images_marginalized)

            # compute probabilities
            (_, probs) = model.infer_batch(batch, calc_probability=True, probability_of_gt=True)

            # marginalize over pixel value (assume uniform distribution)
            marg_prob = sum([probs[i] * pixel_prob[i] for i in range(len(gray_values))])

            pixel_relevance[x, y] = weight_of_evidence(orig_prob, marg_prob)

            print(x, y, pixel_relevance[x, y], orig_prob, marg_prob)

    np.save(Constants.fnPixelRelevance, pixel_relevance)


def analyze_translation_invariance():
    # setup model
    model = Model(open(Constants.fnCharList).read(), DecoderType.BestPath, mustRestore=True)

    # read image and specify ground-truth text
    img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
    (w, h) = img.shape
    assert Model.imgSize[1] == w

    img_list = []
    for dy in range(Model.imgSize[0] - h + 1):
        target_img = np.ones((Model.imgSize[1], Model.imgSize[0])) * 255
        target_img[:, dy:h + dy] = img
        img_list.append(preprocess(target_img, Model.imgSize))

    # put images and gt texts into batch
    batch = Batch([Constants.gtText] * len(img_list), img_list)

    # compute probabilities
    (texts, probs) = model.infer_batch(batch, calc_probability=True, probability_of_gt=True)

    # save results to file
    f = open(Constants.fnTranslationInvarianceTexts, 'wb')
    pickle.dump(texts, f)
    f.close()
    np.save(Constants.fnTranslationInvariance, probs)


def show_results():
    # 1. pixel relevance
    pixel_relevance = np.load(Constants.fnPixelRelevance)
    plt.figure('Pixel relevance')

    plt.imshow(pixel_relevance, cmap=plt.cm.jet, vmin=-0.25, vmax=0.25)
    plt.colorbar()

    img = cv2.imread(Constants.fnAnalyze, cv2.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap=plt.cm.gray, alpha=.4)

    # 2. translation invariance
    probabilities = np.load(Constants.fnTranslationInvariance)
    f = open(Constants.fnTranslationInvarianceTexts, 'rb')
    texts = pickle.load(f)
    texts = ['%d:' % i + texts[i] for i in range(len(texts))]
    f.close()

    plt.figure('Translation invariance')

    plt.plot(probabilities, 'o-')
    plt.xticks(np.arange(len(texts)), texts, rotation='vertical')
    plt.xlabel('horizontal translation and best path')
    plt.ylabel('text probability of "%s"' % Constants.gtText)

    # show both plots
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--relevance':
            print('Analyze pixel relevance')
            analyze_pixel_relevance()
        elif sys.argv[1] == '--invariance':
            print('Analyze translation invariance')
            analyze_translation_invariance()
    else:
        print('Show results')
        show_results()
