import cv2 as cv
from PIL import Image
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class PostIt:
    def __init__(self, file_path, language="eng"):
        self.file_path = file_path
        self.img = Image.open(file_path)
        self.width, self.height = self.img.size
        self.num_pixels = self.width * self.height
        self.text = pt.image_to_string(self.img, lang=language)

    def get_color(self):
        r, g, b = (0, 0, 0)
        for x in range(self.width):
            for y in range(self.height):
                red, green, blue = self.img.getpixel((x, y))
                r, g, b = (r + red, g + green, b + blue)

        r, g, b = (r / self.num_pixels, g / self.num_pixels, b / self.num_pixels)
        return r, g, b

    def print_info(self):
        print("Image: {}".format(self.file_path))
        print("  Size: {} x {}".format(self.width, self.height))
        print("  Text: {}".format(self.text))


class FullImage:
    def __init__(self, file_path):
        self.img = cv.imread(file_path, 1)
        self.file_path = file_path
        self.post_its = []

    def totally_not_copied_from_stackoverflow(self, resize_factor=2):
        lab = cv.cvtColor(self.img, cv.COLOR_BGR2LAB)
        l, a, b = cv.split(lab)
        enhanced = cv.createCLAHE(clipLimit=2.0, tileGridSize=(1, 1))
        cl = enhanced.apply(l)
        merged = cv.merge((cl, a, b))
        final_rgb = cv.cvtColor(merged, cv.COLOR_LAB2BGR)
        final_gray = cv.cvtColor(final_rgb, cv.COLOR_RGB2GRAY)
        self.img = cv.resize(final_gray, (0, 0), fx=(1 / resize_factor), fy=(1 / resize_factor))

    def find_post_its(self, resize_factor=2, language="eng"):
        self.totally_not_copied_from_stackoverflow(resize_factor)
        _, threshold = cv.threshold(self.img, 140, 255, cv.THRESH_BINARY_INV)
        contours, _ = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        count = 0
        file = Image.open(self.file_path)
        width, height = file.size

        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if ((width * height) / 2000) < (w * h) < ((width * height) / 10):
                count = count + 1
                x, y, w, h = (x * resize_factor, y * resize_factor, w * resize_factor, h * resize_factor)
                out = file.crop((x, y, x + w, y + h))
                out.save("out/file_{}.png".format(count))
                self.post_its.append(PostIt("out/file_{}.png".format(count)))

    def print_info(self):
        for post_it in self.post_its:
            post_it.print_info()
