import cv2 as cv
from PIL import Image


class PostIt:
    def __init__(self, file_path, rect):
        self.file_path = file_path
        self.rect = rect
        self.text = ''

    def print_info(self):
        print(f"Path: {self.file_path}")
        print(f"Post-It position: ({self.rect[0]}|{self.rect[1]})")
        print(f"Post-It size: ({self.rect[2]}|{self.rect[3]})")
        print(f"Post-It text: {self.text}")


class ImagePrePreprocessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.img = cv.imread(file_path, 1)
        self.post_its = []

    def pre_preprocess(self, resize_factor):
        lab = cv.cvtColor(self.img, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(lab)
        enhanced = cv.createCLAHE(clipLimit=2.0, tileGridSize=(1, 1))
        cl = enhanced.apply(l)
        merged = cv.merge((cl, a, b))
        final_rgb = cv.cvtColor(merged, cv.COLOR_LAB2BGR)
        final_gray = cv.cvtColor(final_rgb, cv.COLOR_RGB2GRAY)
        self.img = cv.resize(final_gray, (0, 0), fx=(1 / resize_factor), fy=(1 / resize_factor))

    def find_post_its(self, resize_factor=2):
        self.pre_preprocess(resize_factor)
        _, threshold = cv.threshold(self.img, 140, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        file = Image.open(self.file_path)
        width, height = file.size
        count = 0

        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if ((width * height) / 999) < (w * h) < ((width * height) / 10):
                x, y, w, h = (x * resize_factor, y * resize_factor, w * resize_factor, h * resize_factor)
                out = file.crop((x, y, x + w, y + h))
                out_path = f"../data/output_{count}.png"
                self.post_its.append(PostIt(out_path, (x, y, w, h)))
                out.save(out_path)
                count = count + 1

    def print_info(self):
        for x in range(len(self.post_its)):
            self.post_its[x].print_info()
            print()

    def find_words(self):
        img = cv.imread('../data/input2.jpg', 0)
        cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU, img)

        contours, image = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        for c in contours:
            # get the bounding rect
            x, y, w, h = cv.boundingRect(c)
            # draw a white rectangle to visualize the bounding rect
            cv.rectangle(img, (x, y), (x + w, y + h), 255, 1)

        cv.drawContours(img, contours, -1, (255, 255, 0), 1)

        cv.imwrite("../data/output.png", img)
