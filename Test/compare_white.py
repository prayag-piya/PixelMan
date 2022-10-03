import glob
from typing import List
from PIL import Image as PILIMAGE
from FileHelpers import csv_helpers
from FileHelpers.image_helpers import get_base_name, get_images_in_folder
from ImageWand.wandy import wand_blacks, wand_exposure_constrast, wand_whites
from ImageWand.wandy_fit import wand_blacks_fit, wand_whites_fit

def test_multiple_exposure(start,end):
    img='Test\\Mustang.png'
    target='test.jpg'
    for i in range(start,end):
        exposure = 0
        constrat = 0
        lr_image=f'C:\Code\Contrast\mustang+2.jpg'
        wand_exposure_constrast(img,exposure,constrat,dest=target)
        diff = image_diff_per(target,lr_image)
        print(constrat,diff)

        
def test_multiple_black():
    img='Test\\Mustang.png'
    target='test.jpg'
    for i in [1,2,17,50,100]:
        blacks = i
        lr_image=f'C:\Code\\blacks\mustang-{blacks}.jpg'
        wand_blacks_fit(img,blacks,target)
        diff = image_diff_per(target,lr_image)
        print(blacks,diff)

def split_text(text):
    return float(text.split('-wand',-1)[0].split("-w",-1)[-1])


def test_multiple_images(src_folder:str,img_folder:str,whites=52,wb='w'):
    """names must be same for the testing images in the 
    source and testing folder
    Eg:
    img_folder = f"C:\Code\carseffect"
    src_folder = f"C:\Code\cars"
    """
    src_list = get_images_in_folder(src_folder)
    new_image = 'temp.jpg'
    # lr_image_folder=f'C:\Code\whites'
    for old_image in src_list:
        lr_image = f"{img_folder}\{get_base_name(old_image)}"
        print(lr_image)
        whites = 52
        if wb=='w':
            wand_whites_fit(old_image,whites,new_image)
        elif wb=='b':
            wand_blacks_fit(old_image,whites,new_image)
        diff = image_diff_per(new_image,lr_image)
        print(whites,diff)



def compare_all_image(src_img_folder,comparing_image_folder,img_format="jpg",start=0):
    """
    Usage:
    compare_all_image("C:\Code\whites","C:\Code\PLR")
    """
    test_images_list = glob.glob(f'{comparing_image_folder}\*.{img_format}')
    data_list=[]
    # source_image_list =  glob.glob(f'{src_img_folder}\*.{img_format}')
    # orig_whites=0
    # for source in source_image_list:
    for i in range(1,101):
        orig_whites = i
        source = f'{src_img_folder}\mustang-{orig_whites}.{img_format}'
        diff = compare_images(source,test_images_list,start)
        start = diff[2]
        data_list.append([orig_whites,split_text(diff[0]),diff[0],diff[1]])
        print([orig_whites,split_text(diff[0]),diff[0],diff[1]])
    csv_helpers.write_csv('data.csv',data_list)
                
def create_test_images(source:str,destination:str,gap=0.1,wb='w'):
    """
    Usage:
    create_test_images(new_image,f"C:\Code\diff",gap=0.001,start=fit_whites[52])
    create_test_images(new_image,"C:\Code\diff")
    """
    for i in range(0,2001):
        whites=i*gap
        whites_str = '%05.2f' % whites
        dest = f'{destination}\mustang-w{whites_str}-wand.jpg'
        if wb=='w':
            wand_whites(source,whites,dest)
        elif wb=='b':
            wand_blacks(source,whites,dest)
        else:
            pass


def compare_images(imgSrc:str,img_list:List,start=0,prev_diff=None):
    if not prev_diff:
        prev_img = img_list[start]
        prev_diff = image_diff_per(imgSrc,prev_img)

    for imgNew in img_list[start:]:
        new_diff = image_diff_per(imgSrc,imgNew)
        index = img_list.index(imgNew)
        if prev_diff < new_diff:
            # if image_diff_per(imgNew,img_list[index+1]) <= new_diff:
            #     new_diff = image_diff_per(imgNew,img_list[index+1])
            # else:
                return (prev_img,prev_diff,index)
        prev_diff = new_diff
        prev_img = imgNew
        print(prev_diff)
    return None

def image_diff_per(imgSrc:str,imgNew:str):
    i1 = PILIMAGE.open(imgSrc)
    i2 = PILIMAGE.open(imgNew)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    
    ncomponents = i1.size[0] * i1.size[1] * 3
    return (dif / 255.0 * 100) / ncomponents

