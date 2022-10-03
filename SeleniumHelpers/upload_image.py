from SeleniumHelpers.helpers import get_driver,Login2Portal,get_vin_link,upload_image_to_link,goto_url

driver_path ='C:\\Code\\PixelMan\\SeleniumHelpers\\geckodriver.exe'
pm_user="mojyezer"
pm_pass="Justpass1"
login_url = 'https://dmsapp.dealercenter.net/home/postsignin'
inventory_url = 'https://app.dealercenter.net/report/dashboard/inventoryreport/active-inventory-report'

def upload_given_vin(vin_number):
    my_driver = get_driver(driver_path)
    Login2Portal(my_driver,pm_user,pm_pass,login_url)
    goto_url(my_driver,inventory_url)
    vin_link = get_vin_link(my_driver,vin_number)
    goto_url(my_driver,vin_link)
    upload_image_to_link(my_driver)