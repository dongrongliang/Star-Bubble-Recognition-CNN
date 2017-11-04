import os, re
import math
from PIL import Image

test=Image.open('./test_pic.jpeg')

def crop(infile,height,width):
    im = Image.open(infile)
    imgwidth, imgheight = im.size
    for i in range(imgheight//height):
        for j in range(imgwidth//width):
            box = (j*width, i*height, (j+1)*width, (i+1)*height)
            yield im.crop(box)

infile='./test_pic.jpeg'
height=200
width=200
start_num=1
for k,piece in enumerate(crop(infile,height,width),start_num):
    img=Image.new('RGB', (height,width), 255)
    img.paste(piece)
    img.save("./test/predict/pic%03d.jpg" % k, format="JPEG")