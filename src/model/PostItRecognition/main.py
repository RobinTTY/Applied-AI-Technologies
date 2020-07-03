from PIL import Image
import numpy as np


def convert_image(file_path):
    img = Image.open(file_path)
    img = img.convert("L").resize((128, int(img.size[1] * (128 / img.size[0]))))
    if img.size[1] > 32:
        img = img.resize((int(img.size[0] * (32 / img.size[1])), 32))
    img = Image.fromarray(np.where(np.array(img) > np.array(img)[0][0] - 20, 255, 0))
    bg = Image.new('RGBA', (128, 32), (255, 255, 255, 255))
    bg.paste(img, (0, 0))
    return bg


res = convert_image("test1.png")
res.show()
# res.save("output.png")
