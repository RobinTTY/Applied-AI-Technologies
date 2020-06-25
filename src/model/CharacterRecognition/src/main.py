from __future__ import division
from __future__ import print_function

import sys
import argparse
import cv2
from DataLoader import DataLoader, Batch
from Model import Model, DecoderType
from SamplePreprocessor import preprocess


class FilePaths:
	"""relevant file paths"""
	fnCharList = '../model/charList.txt'
	fnAccuracy = '../model/accuracy.txt'
	fnInfer = '../data/test.png'


def extract_text(model, input_img):
	"""recognize text in image provided by file path"""
	img = preprocess(cv2.imread(input_img, cv2.IMREAD_GRAYSCALE), Model.imgSize)
	batch = Batch(None, [img])
	(recognized, probability) = model.infer_batch(batch, True)
	print('Recognized:', '"' + recognized[0] + '"')
	print('Probability:', probability[0])


def main():
	# optional command line args
	parser = argparse.ArgumentParser()
	parser.add_argument('--train', help='train the NN', action='store_true')
	parser.add_argument('--validate', help='validate the NN', action='store_true')
	parser.add_argument('--beamsearch', help='use beam search instead of best path decoding', action='store_true')
	parser.add_argument('--wordbeamsearch', help='use word beam search instead of best path decoding', action='store_true')
	parser.add_argument('--dump', help='dump output of NN to CSV file(s)', action='store_true')

	args = parser.parse_args()

	decoder_type = DecoderType.BestPath

	# infer text on test image
	print(open(FilePaths.fnAccuracy).read())
	model = Model(open(FilePaths.fnCharList).read(), decoder_type, must_restore=True, dump=args.dump)
	extract_text(model, FilePaths.fnInfer)


if __name__ == '__main__':
	main()

