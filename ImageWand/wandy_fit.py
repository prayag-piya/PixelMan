from wand.image import Image
from Exceptions.Errors import ValueNotInRangeError
# 20.84
fit_whites = [None,2,2,2,2,2.7,2.9,2.9,2.9,3,3,3,5.2,5.3,5.4,5.5,6.3,6.3,6.3,6.4,7.2,7.3,7.4,8,8.1,8.2,8.7,8.8,9.1,9.6,9.6,9.8,10.3,10.7,10.9,11.2,11.7,11.7,12.4,12.6,13.2,13.4,14,14.5,14.6,15.8,16.2,17.3,17.5,19,19.1,20.8,20.84,22.6,23.2,24.1,24.2,26.4,28,28.3,32.3,32.5,32.8,36.6,36.6,40.3,41.5,43.4,44.5,45.9,45.9,48.2,49,50.3,50.9,51.9,52.6,54.3,54.3,55.3,55.9,55.9,57,58,59.3,60.2,60.6,62.3,65.6,66.4,69,69.4,69.4,73.6,76,77.1,77.6,84.8,93.6,93.6,93.6]
fit_blacks =[None,2,1.2,2,2,2.7,2.9,2.9,2.9,3,3,3,5.2,5.3,5.4,5.5,6.3,6.3,6.3,6.4,7.2,7.3,7.4,8,8.1,8.2,8.7,8.8,9.1,9.6,9.6,9.8,10.3,10.7,10.9,11.2,11.7,11.7,12.4,12.6,13.2,13.4,14,14.5,14.6,15.8,16.2,17.3,17.5,19,19.1,20.8,20.84,22.6,23.2,24.1,24.2,26.4,28,28.3,32.3,32.5,32.8,36.6,36.6,40.3,41.5,43.4,44.5,45.9,45.9,48.2,49,50.3,50.9,51.9,52.6,54.3,54.3,55.3,55.9,55.9,57,58,59.3,60.2,60.6,62.3,65.6,66.4,69,69.4,69.4,73.6,76,77.1,77.6,84.8,93.6,93.6,221.2]

def wand_blacks_fit(img_loc:str,blacks_val:int,dest=None):
    if blacks_val not in range(0,101):
        raise ValueNotInRangeError("blacks_val",blacks_val,0,100)
    blacks=fit_whites[blacks_val]*2.3
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.contrast_stretch(white_point=0,black_point=blacks/1000,channel='all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def wand_whites_fit(img_loc:str,whites_val:int,dest=None):
    if whites_val not in range(0,101):
        raise ValueNotInRangeError("whites_val",whites_val,0,100)
    whites=fit_whites[whites_val]
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.contrast_stretch(black_point=0,white_point=whites/1000,channel='all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image


def wand_exposure_constrast_fit(img_loc:str,exposure_val:float=0,contrast_val:float=0,dest:str=None):
    """AI is creating summary for wand_exposure_constrast

    Args:
        img_loc (str): [description]
        exposure_val (float, optional): -5 <- 0 -> +5. Defaults to 0.
        contrast_val (int, optional): -100 <- 0 -> +100. Defaults to 0.
        dest (str, optional): Save the image with this Location. Defaults to returns the image object
    Returns:
        [type]: Return Image or Saved Image Location
    """
    # contrast upper limit: -19 to 19
    if exposure_val not in range(-5,5):
        raise ValueNotInRangeError("exposure_val",exposure_val,-5,5)
    if contrast_val not in range(-101,101):
        raise ValueNotInRangeError("contrast_val",contrast_val,-100,100)
    exposure_val= exposure_val*16.5 if -10>exposure_val>10 else exposure_val*27.5
    contrast_val=contrast_val*2*0.28 if -10>contrast_val>10 else contrast_val*2.56
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.brightness_contrast(exposure_val,contrast_val,'all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def wand_sharpness(filename:str, amount:int, radius:float,elevation_val,dest=None)->Image:
    """
    AI is creating summary for sharpness
    Args:
        filename ([str]): [description]
        amount ([float]): 1-150
        radius ([float]): 0.1-3.1
    """
    with Image(filename=filename) as img:
        with img.clone() as temp_image:
            # temp_image.sharpen(radius=radius/100, sigma=amount)
            temp_image.shade(elevation=elevation_val)
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def wand_saturation_fit(filename:str, value:float)->Image:
    """
    AI is creating summary for saturation
    Args:
        filename ([str]): [description]
        value ([float]): [description]
    """
    if value not in range(-101,101):
        raise ValueNotInRangeError("saturation",value,-100,100)
    value = value+100
    with Image(filename=filename) as img:
        img.modulate(saturation = value)
        return img
