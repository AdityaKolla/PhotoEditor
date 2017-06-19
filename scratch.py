from PIL import Image
import os
import numpy
os.chdir('C:\\Users\Rahtoken\Documents\Composite')
#arse = Image.open('arse.jpg')
#width, height = arse.size
#if width < height:
 #   new_size = width
#else:
 #   new_size = height

def make_1024(src):
    res = src.resize((1024,1024))
    return res

#new_arse = make_1024(arse)
#new_arse.save('new_arse.jpg')
arse1 = Image.open('arse1.jpg')
new_arse1=make_1024(arse1)
new_arse1.save('new_arse1.jpg')
arse2 = Image.open('arse2.jpg')
new_arse2=make_1024(arse2)
new_arse2.save('new_arse2.jpg')
arse3 = Image.open('arse3.jpg')
new_arse3 = make_1024(arse3)
new_arse3.save('new_arse3.jpg')
arse4= Image.open('arsefinal.jpg')
new_arse4=make_1024(arse4)
new_arse4.save('new_arse4.jpg')

def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image

def fetch_pixel(img,xpx,ypx):
    pixel = img.getpixel((xpx,ypx))
    return pixel

img_list=[new_arse1,new_arse2,new_arse3,new_arse4]
final = Image.open('arse4.jpg')
new_final = make_1024(final)
new_final.save('new_finalarse.jpg')

def magic(img_list,width,height):
    result = create_image(width,height)
    pixels = result.load()
    i = 3
    x = 0
    y = 0
    for x in range(1024):
        for y in range(1024):
            px = fetch_pixel(img_list[i],x,y)
            pixels[x,y] = px
            i = i - 1
            if i < 0 :
                i = 3
    return result

res = magic(img_list,1024,1024)
res.save('result.jpg')

def parse_list(to_parse,x,y):
    pixels = []
    for img in to_parse:
        pixels = pixels + [fetch_pixel(img,x,y)]
    return pixels

def closest_pixel(src_pixels,target_pixel):
    dump = []
    for x in src_pixels:
        dump = dump + [tuple(numpy.subtract(x,target_pixel))]
    mod_dump = []
    for x in dump:
        mod_dump = mod_dump + [tuple(numpy.abs(x))]
    mod_dump.sort()
    i = 1
    z = mod_dump[0]
    while i < 4 :
        if mod_dump[i] == 0:
            mod_dump[0] = mod_dump[i]
        i += 1
    for y in src_pixels:
        if (tuple(numpy.abs(tuple(numpy.subtract(y,target_pixel))))) == mod_dump[0]:
            return y

def composite(src_list,target):
    result = create_image(1024, 1024)
    pixels = result.load()
    for x in range(1024):
        for y in range(1024):
            src_pixels = parse_list(src_list,x,y)
            target_pixel = fetch_pixel(target,x,y)
            res_pixel = closest_pixel(src_pixels,target_pixel)
            pixels[x,y] = res_pixel
    return result

fin = composite(img_list,new_final)
fin.save('itworks.jpg')
Image._show(fin)

