from cv2 import extractChannel
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .implicit_helpers import click_when_loaded,search_when_loaded
import time
import os
import glob
import ntpath

# Global Variables

# put all the profile in the profiles folder
PROFILE_DIR = 'profiles'
IMP_DELAY = 10

# Initialize the driver object
def get_driver(driver_path,zoom_level=1.35):
    """ 
    Description: New Instance of the webbrowser with given profile
    Input: 
        profile: <current profile instance>
    Output:
        Instance of the new browser
    """  
    
    options = FirefoxOptions()
    # options.add_argument("--headless")
    fp = webdriver.FirefoxProfile()
    # zoomed out because sometimes skip button was out of view 
    fp.set_preference("layout.css.devPixelsPerPx", str(zoom_level))
    pixelbot = webdriver.Firefox(executable_path=driver_path,firefox_profile=fp,options=options)
    pixelbot.maximize_window()
    return pixelbot


def Login2Portal(pixelbot:webdriver,username:str,password:str,BASE_URL:str):
    """Creating summary for portal access
    Args:
        username (str): [description]
        password (str): [description]
    """
    pixelbot.get(BASE_URL)
    userNm = pixelbot.find_element_by_name('userName')
    userNm.send_keys(username)
    authKey = pixelbot.find_element_by_name('password')
    authKey.send_keys(password)
    authKey.send_keys(Keys.RETURN)

def goto_url(pixelbot,url:str):
    """AI is creating summary for goto_url

    Args:
        pixelbot ([type]): [description]
        url (str): [description]
    """
    time.sleep(10)
    js_command = f"window.location.assign('{url}')"
    pixelbot.execute_script(js_command)

def get_href(pixelbot,xpath):
    return pixelbot.find_element(By.XPATH,xpath).get_attribute('href') 

def goto_vin_using_js(pixelbot,vin_number:str):
    vin_locator='input.lookup-textbox'
    search_query=f"document.querySelectorAll('{vin_locator}')[0].value='{vin_number}'"
    try:
        pixelbot.execute_script(pixelbot,search_query)
    except:
        print("Execute Script Error")

def click_if_one(pixelbot,css_selector_to_click:str,position:int=0,retry:int=15):
    click_query = f"document.querySelectorAll('{css_selector_to_click}')[{position}].click()"
    for i in range(1,retry):
        try:
            if int(pixelbot.execute_script(f"return document.querySelectorAll('{css_selector_to_click}').length"))==1:
                pixelbot.execute_script(click_query)
                # pixelbot.execute_script(document.querySelectorAll('dc-lookup-inventory-item')[0]
                return 'done'
        except:
            time.sleep(1)
            print(f"Wait 1 second for {i}")
    return 0  

def click_if_two(pixelbot,css_selector_to_click:str,position:int=1,retry:int=5):
    click_query = f"document.querySelectorAll('{css_selector_to_click}')[{position}].click()"
    for i in range(1,retry):
        if int(pixelbot.execute_script(f"return document.querySelectorAll('{css_selector_to_click}').length"))==2:
                pixelbot.execute_script(click_query)
                # pixelbot.execute_script(document.querySelectorAll('dc-lookup-inventory-item')[0]
                return 'done'
        else:
            time.sleep(1)
            print(f"Wait 1 second for {i}")
    return 0

def get_vin_link(pixelbot,vin:str)->str:
    """AI is creating summary for get_vin_link

    Args:
        pixelbot ([type]): [description]
        vin (str): [description]

    Returns:
        str: link to the vin upload portal
    """
    vin_input_xpath='//dc-lookup//input'
    vin_lookup_xpath = "//div[@class='lookup-dialog-overlay-items']//dc-lookup-item[1]"
    vin_run_filter_btn_xpath = '//kendo-panelbar-item//button[contains(text(),"Run")]'
    vin_div_with_link_xpath = '//dc-vehicle-template/div[1]/div/div/a'

    click_when_loaded(pixelbot,vin_input_xpath)
    search_when_loaded(pixelbot,vin_input_xpath,vin)
    # click_when_loaded(pixelbot,vin_lookup_xpath)
    # click using js because selenium was full of shit when trying to locate the overlay or I was dumb
    # wait two second to give it time to search the thingys
    click_if_one(pixelbot,'dc-lookup-inventory-item')

    click_when_loaded(pixelbot,vin_run_filter_btn_xpath)
    vin_link = get_href(pixelbot,vin_div_with_link_xpath)
    return vin_link

def select_all_and_upload(image_location_folder,images_in_str):
    import autoit
    autoit.win_wait_active("File Upload", 3)
    autoit.control_set_text("File Upload","Edit1",image_location_folder)
    time.sleep(1)
    autoit.control_click("File Upload","Button1")
    time.sleep(1)
    autoit.control_set_text("File Upload","Edit1",images_in_str)
    time.sleep(1)
    autoit.control_click("File Upload","Button1")


def upload_image_to_link(pixelbot:webdriver,image_location_folder:str=None,image_format=('png','jpg',"jpeg","gif","ico")):
    """AI is creating summary for upload_image_to_link

    Args:
        pixelbot ([type]): [description]
        image_path_list (list): [description]
    """
    image_list=[]
    images_list_as_str=""
    image_location_folder = r'C:\LaudaUploader\.Temp'

    online_marketing_tab_btn = '//span[contains(text(),"Online Marketing")]/..'
    upload_photos_btn = '//div[@class="addPhotos"]/span[2]'
    unwanted_popup_close_btn = 'a.k-window-action.k-link'
    save_btn = '//a[@class="cc-ribbon-item at__inventory_vehicledetails_sidebar_savebutton"]'
    for format in image_format:
        image_list= image_list+glob.glob(os.path.join(image_location_folder,f'*.{format}'))
    for images in image_list:
        images_list_as_str = images_list_as_str+f'"{ntpath.basename(images)}" '
    click_when_loaded(pixelbot,online_marketing_tab_btn)
    time.sleep(4)
    click_if_two(pixelbot,unwanted_popup_close_btn,1)
    click_when_loaded(pixelbot,upload_photos_btn)
    import pdb;pdb.set_trace()
    select_all_and_upload(image_location_folder,images_list_as_str[:-1])
    click_when_loaded(pixelbot,save_btn)