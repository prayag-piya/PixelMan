from wand.image import Image

def wand_whites(img_loc:str,whites_val:int,dest:str=None):
    """AI is creating summary for wand_whites

    Args:
        img_loc (str): [description]
        whites_val (int): [description]
        dest (str, optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    whites=whites_val
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.contrast_stretch(black_point=0,white_point=whites/1000,channel='all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image


def wand_blacks(img_loc:str,blacks_val:int,dest:str=None):
    """AI is creating summary for wand_blacks

    Args:
        img_loc (str): [description]
        blacks_val (int):  0 -> +100. Defaults to 0.
        dest (str, optional): Save the image with this Location. Defaults to returns the image object
    Returns:
        [type]: Return Image or Saved Image Location
    """
    blacks=blacks_val*2.36
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.contrast_stretch(white_point=0,black_point=blacks/1000,channel='all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image


def wand_exposure_constrast(img_loc:str,exposure_val:float=0,contrast_val:float=0,dest:str=None):
    """AI is creating summary for wand_exposure_constrast

    Args:
        img_loc (str): [description]
        exposure_val (float, optional): -5 <- 0 -> +5. Defaults to 0.
        contrast_val (int, optional): -100 <- 0 -> +100. Defaults to 0.
        dest (str, optional): Save the image with this Location. Defaults to returns the image object
    Returns:
        [type]: Return Image or Saved Image Location
    """
    exposure_val=exposure_val
    contrast_val=contrast_val
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.brightness_contrast(exposure_val, contrast_val, 'all_channels')
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def saturation(filename:str, value:float)->Image:
    """
    AI is creating summary for saturation
    Args:
        filename ([str]): [description]
        value ([float]): [description]
    """
    with Image(filename=filename) as img:
        img.modulate(saturation = value)
        return img

def wand_shadow(img_loc:str,alpha:float=0,gamma:float=0,dest:str=None,x=0,y=0):
    """AI is creating summary for wand_exposure_constrast

    Args:
        img_loc (str): [description]
        exposure_val (float, optional): -5 <- 0 -> +5. Defaults to 0.
        contrast_val (int, optional): -100 <- 0 -> +100. Defaults to 0.
        dest (str, optional): Save the image with this Location. Defaults to returns the image object
    Returns:
        [type]: Return Image or Saved Image Location
    """
    alpha=alpha
    gamma=gamma
    with Image(filename=img_loc) as img:
        with img.clone() as temp_image:
            temp_image.shadow(alpha,gamma,x,y)
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def wand_sharpness(filename:str, amount:int, radius:float, azimuth:float,elevation:float,dest=None)->Image:
    """
    AI is creating summary for sharpness
    Args:
        filename ([str]): [description]
        amount ([float]): 1-150
        radius ([float]): 0.1-3.1
    """
    with Image(filename=filename) as img:
        with img.clone() as temp_image:
            # temp_image.sharpen(radius=radius, sigma=amount)
            img.shade(azimuth=azimuth, elevation=elevation)

            # temp_image.shade(elevation=elevation_val)
            if dest:
                temp_image.compression_quality = 99
                temp_image.save(filename=dest)
            else:
                return temp_image

def details(filename:str, azimuth:float, elevation:float)->Image:
    """AI is creating summary for details
    Args:
        filename (str): [description]
        azimuth (float): [value azimuth describe X/Y value of the image]
        elevation (float): [Value elevation describe Z value of the image with give image a 3D like effect]
    """
    with Image(filename=filename) as img:
        img.shade(gray=True, azimuth=azimuth, elevation=elevation)
        return img

def masking(filename:str, radius:float, sigma:float):
    """AI is creating summary for masking
    Args:
        filename (str): [description]
        radius (float): [description]
        sigma (float): [description]
    """
    with Image(filename=filename) as img:
        img.emboss(radius=radius, sigma=sigma)
        return img
        