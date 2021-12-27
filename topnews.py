import requests
import qrcode
from PIL import Image

img = qrcode.make("https://pypi.org/project/qrcode/")

img.save("test.png")

Image.open(img)
