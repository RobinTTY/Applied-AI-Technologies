import os
import cv2
import opencv_wrapper as cvw
from WordSegmentation import segment_word, prepare_img


def main():
	image = cv2.imread("../data/example2.jpg")

	gray = cvw.bgr2gray(image)
	thresh = cvw.threshold_otsu(gray, inverse=True)

	# dilation
	img_dilation = cvw.dilate(thresh, 5)

	# Find contours
	contours = cvw.find_external_contours(img_dilation)
	# Map contours to bounding rectangles, using bounding_rect property
	rects = map(lambda c: c.bounding_rect, contours)
	# Sort rects by top-left x (rect.x == rect.tl.x)
	sorted_rects = sorted(rects, key=lambda r: r.x)

	# Distance threshold
	dt = 80

	# List of final, joined rectangles
	final_rects = [sorted_rects[0]]

	# mine
	sum = 0
	for rect in sorted_rects:
		sum += rect.x

	sum /= len(sorted_rects)
	print(sum)
	#dt = sum
	# mine

	for rect in sorted_rects[1:]:
		prev_rect = final_rects[-1]

		# Shift rectangle `dt` back, to find out if they overlap
		shifted_rect = cvw.Rect(rect.tl.x - dt, rect.tl.y, rect.width, rect.height)
		cvw.rectangle(image, shifted_rect, cvw.Color.BLACK, thickness=2)
		# print("shifted rect:" + str(shifted_rect.x) + "-" + str(shifted_rect.x + shifted_rect.width))
		# print("prev rect:" + str(prev_rect.x) + "-" + str(prev_rect.x + prev_rect.width))
		if((shifted_rect & prev_rect).area() > 0):
			print("intersect")
		intersection = cvw.rect_intersection(prev_rect, shifted_rect)
		if intersection is not None:
			print("intersect")
			# Join the two rectangles
			min_y = min((prev_rect.tl.y, rect.tl.y))
			max_y = max((prev_rect.bl.y, rect.bl.y))
			max_x = max((prev_rect.br.x, rect.br.x))
			width = max_x - prev_rect.tl.x
			height = max_y - min_y
			new_rect = cvw.Rect(prev_rect.tl.x, min_y, width, height)
			# Add new rectangle to final list, making it the new prev_rect
			# in the next iteration
			final_rects[-1] = new_rect
		else:
			# If no intersection, add the box
			final_rects.append(rect)

	for rect in sorted_rects:
		cvw.rectangle(image, rect, cvw.Color.MAGENTA, line_style=cvw.LineStyle.DASHED)

	for rect in final_rects:
		cvw.rectangle(image, rect, cvw.Color.GREEN, thickness=2)

	cv2.imwrite("../data/result.png", image)


def test():
	"""reads images from data/ and outputs the word-segmentation to out/"""
	# read input images from 'in' directory
	img_files = os.listdir('../data/')
	for (i, f) in enumerate(img_files):
		print('Segmenting words of sample %s' % f)

		# read image, prepare it by resizing it to fixed height and converting it to grayscale
		img = prepare_img(cv2.imread('../data/%s' % f), 50)

		# execute segmentation with given parameters
		# -kernelSize: size of filter kernel (odd integer)
		# -sigma: standard deviation of Gaussian function used for filter kernel
		# -theta: approximated width/height ratio of words, filter function is distorted by this factor
		# - minArea: ignore word candidates smaller than specified area
		res = segment_word(img, kernel_size=25, sigma=11, theta=7, min_area=100)

		# write output to 'out/inputFileName' directory
		if not os.path.exists('../out/%s' % f):
			os.mkdir('../out/%s' % f)

		# iterate over all segmented words
		print('Segmented into %d words' % len(res))
		for (j, w) in enumerate(res):
			(wordBox, wordImg) = w
			(x, y, w, h) = wordBox
			# save word
			cv2.imwrite('../out/%s/%d.png' % (f, j), wordImg)
			# draw bounding box in summary image
			cv2.rectangle(img, (x, y), (x+w, y+h), 0, 1)

		# output summary image with bounding boxes around words
		cv2.imwrite('../out/%s/summary.png' % f, img)


if __name__ == '__main__':
	main()
