from os import listdir
from PIL import Image

ims = [Image.open(fn) for fn in listdir() if fn.endswith('.png')]

width,height = ims[0].size

result = Image.new(ims[0].mode, (width, height*len(ims)))

for i,im in enumerate(ims):
    result.paste(im,box=(0,i*height))

    result.save('result.png')