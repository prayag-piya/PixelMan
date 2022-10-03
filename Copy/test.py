def get_whites_only(img):
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    return img.putdata(newData)


def get_pixel_white(raw_image,opacity:int=1):
    img_height = raw_image.height
    img_width = raw_image.width
    for h in range(img_height):
        for w in range(img_width):
            coordinate = w,h
            if raw_image.getpixel(coordinate)!=(255, 255, 255,):
                raw_image.putpixel(coordinate,(255, 255, 255,0))
            # else:
            #     print(coordinate)


    return raw_image

def get_pixel_black(raw_image,opacity:int=1):
    img_height = raw_image.height
    img_width = raw_image.width
    for h in range(img_height):
        for w in range(img_width):
            coordinate = w,h
            if raw_image.getpixel(coordinate)!=(0, 0, 0):
                raw_image.putpixel(coordinate,(255, 255, 255, 0))
            # else:
            #     print(coordinate)

    return raw_image


from PIL import Image, ImageColor, ImageDraw, ImageEnhance


def highlight_whites_area(img, factor):
    """ Highlight specified rectangular region of image by `factor` with an
        optional colored  boarder drawn around its edges and return the result.
    """
    temp_image = img.copy()  # Avoid changing original image.
    brightner = ImageEnhance.Brightness(temp_image)
    # factor is between 1 to 1.5 for white
    temp_image = brightner.enhance(factor+1)
    return temp_image

def get_whites_only(img_real,opacity=2):
    img = img_real.copy()
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y][0:-1] != (255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    return blend_image(img_real,img,opacity)

def get_blacks_only(img_real,opacity=16):
    img = img_real.copy()
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y][0:-1] != (0, 0, 0):
                pixdata[x, y] = (0, 0, 0, 0)
    return blend_image(img_real,img,opacity)

def create_transparent_image_black():
    img = Image.open('image.png')
    rgba = img.convert("RGBA")
    datas = rgba.getdata()
    
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
            # storing a transparent value when we find a black colour
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)  # other colours remain unchanged
    
    rgba.putdata(newData)
    rgba.save("transparent_image.png", "PNG")

import PIL
from PIL import Image

from libxmp import XMPFiles, consts
from libxmp.utils import file_to_dict

def copy_xml(source:str,dest:str):
    new_image = PIL.Image.new(mode="RGB", size=(200, 200))
    new_image.save(dest)

    xmpfile = XMPFiles(file_path = source, open_forupdate = True)
    xmpfile2 = XMPFiles(file_path = dest, open_forupdate = True)

    xmp = xmpfile.get_xmp()
    xmpfile2.put_xmp(xmp)
    xmpfile2.can_put_xmp(xmp)

    xmpfile.close_file()
    xmpfile2.close_file()