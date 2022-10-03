from asyncio.windows_events import NULL
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def click_element(pixelbot,element_to_click:str):
    """AI is creating summary for click_element

    Args:
        pixelbot ([type]): [description]
        element_to_click (str): [description]
    """
    pixelbot.find_element(By.XPATH,element_to_click).click()

def search_text(pixelbot,search_box:str,search_text:str):
    """AI is creating summary for search_text

    Args:
        pixelbot ([type]): [description]
        search_box (str): [description]
        search_text (str): [description]
    """
    click_element(pixelbot,search_box)
    input = pixelbot.find_element(By.XPATH,search_box)
    # Click the button to visit sites
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.DELETE)
    input.send_keys(search_text)
    input.send_keys(Keys.ENTER)

def click_when_loaded(pixelbot,xpath_to_click:str,total_wait:int=20,refresh_time:int=1):
    """AI is creating summary for click_when_loaded

    Args:
        pixelbot ([type]): <current tab instance>
        xpath_to_click (str): xpath of the element to click
        total_wait (int, optional): Time interval to refresh the page if element not found in seconds. Defaults to 20.
        refresh_time (int, optional): Time to wait before trying again Defaults to 2.

    Returns:
        [type]: [description]
    """
    while total_wait>0:
        try:
            my_element = pixelbot.find_element(By.XPATH,xpath_to_click)
            my_element.click()
            return pixelbot.find_element(By.XPATH,xpath_to_click)
        except:
            print(f'Waiting {refresh_time} seconds more until {xpath_to_click} loads')
            time.sleep(refresh_time)
            total_wait=total_wait-refresh_time
    return NULL

def search_when_loaded(pixelbot,xpath_to_search:str,search_text,total_wait:int=20,refresh_time:int=2):
    """AI is creating summary for click_when_loaded

    Args:
        pixelbot ([type]): <current tab instance>
        xpath_to_click (str): xpath of the element to click
        total_wait (int, optional): Time interval to refresh the page if element not found in seconds. Defaults to 20.
        refresh_time (int, optional): Time to wait before trying again Defaults to 2.

    Returns:
        [type]: [description]
    """
    while total_wait>0:
        try:
            pixelbot.find_element(By.XPATH,xpath_to_search).click()
            pixelbot.find_element(By.XPATH,xpath_to_search).send_keys(search_text)
            time.sleep(5)
            pixelbot.find_element(By.XPATH,xpath_to_search).send_keys(Keys.ENTER)
            return "element_loaded"
        except:
            print(f'Waiting {refresh_time} seconds more until {xpath_to_search} loads')
            time.sleep(refresh_time)
            total_wait=total_wait-refresh_time
    import pdb; pdb.set_trace()
    return total_wait


def wait_until_load(fxn,total_wait:int=20,refresh_time:int=2):
    """AI is creating summary for search_vin_number

    Args:
        fxn ([type]): <current tab instance>
        total_wait (int, optional): Time interval to refresh the page if element not found in seconds. Defaults to 20.
        refresh_time (int, optional): Time to wait before trying again Defaults to 2.

    Returns:
        [type]: [description]
    """
    myfxn = fxn()
    loaded = 0
    while loaded<0:
        try:
            myfxn()
            loaded=0
            return "element_loaded"
        except:
            print(f'Waiting {refresh_time} seconds more until elements loads')
            time.sleep(refresh_time)
            loaded=total_wait-refresh_time
    print(loaded)
    return loaded
    
def goto_url(pixelbot,url:str):
    """AI is creating summary for goto_url

    Args:
        pixelbot ([type]): [description]
        url (str): [description]
    """
    time.sleep(2)
    js_command = f"window.location.assign('{url}')"
    pixelbot.execute_script(js_command)