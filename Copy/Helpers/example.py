from Helpers.helpers import blend_image, get_black_n_white, get_blacks_only, get_whites_only, get_image_local, put_image_local
from Helpers.xmpHelper import copy_xmp,read_xmp
# show the given image using local image processor
# show_image('Test\\160824.jpg')
source = 'car3.jpg'
dest = 'new.jpg'

copy_xmp(source)
# load the image into an pillow array
# pil_image_arr = get_image_local('Test\\car2.jpg').convert("RGB")
# white_filter = get_image_local('Test\\new.png')
# # create whites for white filter
# filter_1 = get_whites_only(pil_image_arr,5)
# filter_2 = get_blacks_only(pil_image_arr,16)

# pil_image_arr.show()
# filter_1.show()
# filter_2.show()

# put_image_local(filter_1,"white.png")
# put_image_local(filter_2,"black.png")
# print(pil_image_arr.size)
# print(white_filter.size)
# image_with_wb_filter = blend_image(pil_image_arr,white_filter,0.4)

# pil_image_arr.show()
# image_with_wb_filter.show()
# whites +2
# blacks +16

# new_image = put_image_local(white_filter,'Test\\new.jpg')
# save the image_array to a image file in the given locaiton