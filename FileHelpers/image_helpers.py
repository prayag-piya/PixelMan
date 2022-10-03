import os,glob
def get_images_in_folder(img_folder,img_format="jpg"):
    return glob.glob(f'{img_folder}\*.{img_format}')

def get_base_name(file_path):
    return os.path.basename(file_path)