import pyexiv2


my_xmp_filter= ""
def copy_xmp(image_loc:str,xmp_dict:any=my_xmp_filter):
    img = pyexiv2.Image(image_loc)
    img.modify_xmp(xmp_dict)
    img.close()

def read_xmp(image_loc:str):
    with pyexiv2.Image(image_loc) as img:
        data = img.read_xmp()
    return data