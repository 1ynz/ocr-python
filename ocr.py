import pyocr
import pyocr.builders
from PIL import Image

#init OCR

tool = pyocr.get_available_tools()[0]
lang = tool.get_available_languages()[0]
print(lang)
img = Image.open('uccu.jpg')

ans = tool.image_to_string(img, lang=lang, builder=pyocr.builders.TextBuilder())

