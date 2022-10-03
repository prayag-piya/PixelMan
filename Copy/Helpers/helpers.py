from errno import ESTALE
import numpy as np
from PIL import Image
from PIL import ImageStat

def show_image(imageLocation:str):
    with Image.open(imageLocation) as im:
        im.show()

def get_image_info(imagePIL):
    with Image.open(imagePIL) as im:
        im_size = im.size
        im_format = im.format
    return (im_size,im_format)

def get_image_local(myImage:str, mode="RGBA")->any:
    im = Image.open(myImage).convert(mode)
    # np_image_array = np.asarray(im)
    # pillow_image_array = Image.fromarray(np_image_array,mode=mode)
    return im

def get_image_histogram(myImage:str)->str:
    return ImageStat.Stat(myImage)

def put_image_local(raw_image,outLocation:str)->any:
    raw_image.save(outLocation)
    return outLocation

def new_image(raw_image,outLocation:str)->any:
    raw_image.save(outLocation)

def get_black_n_white(raw_image:Image):
    return raw_image.convert('L').convert("RGBA") # convert image to black and white


def resize(image:str, size:tuple):
    """
    Resize an image to a given size.
    :prarm image: The image to resize.
    :param size: The size to resize the image to.
    :return: The resized image.
    """
    im = Image.open(image)
    im.thumbnail(size, Image.ANTIALIAS)
    return im

def get_whites_only(img_real,opacity=2):
    opacity=int(2.25*opacity)
    img = img_real.copy()
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y][0:-1] == (255, 255, 255):
                pixdata[x, y] = (255, 255, 255, opacity)
            else:
                pixdata[x, y] = (255, 255, 255, 0)

    # return img
    return blend_image(img_real,img,0.99)

def get_blacks_only(img_real,opacity=16):
    opacity=int(2.25*opacity)
    img = img_real.copy()
    pixdata = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y][0:-1] == (0, 0, 0):
                pixdata[x, y] = (0, 0, 0, opacity)
            else:
                pixdata[x, y] = (255, 255, 255, 0)

    # return img
    return blend_image(img_real,img,0.99)

def blend_image(image_1,image_filter,effect=0.001):
    return Image.blend(image_1,image_filter,effect)