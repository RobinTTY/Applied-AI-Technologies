from PIL import Image


def convert_image(file_path):
    img = Image.open(file_path)
    factor = 128 / img.size[0] if abs(1 - (128 / img.size[0])) > abs(1 - (32 / img.size[1])) else 32 / img.size[1]
    img = img.resize((int(img.size[0] * factor), int(img.size[1] * factor))).convert("L")
    bg = Image.new('RGBA', (128, 32), (255, 255, 255, 255))
    bg.paste(img, (0, 0))
    return bg


res = convert_image("test.png")
res.show()
# res.save("output.png")
