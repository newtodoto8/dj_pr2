from multiprocessing.connection import wait
from time import time
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(executable_path=ChromeDriverManager().install())
import os
v=r"C:\Users\user\Documents\garbage\python\selenium\chromedriver_win32"
os.environ['PATH']+=os.path.abspath(v)

driver = webdriver.Chrome()
driver.get('https://videshapps.gov.in/videsh/login')
a=driver.find_element_by_id('email')
a.send_keys('vcrsection@mea.gov.in')
b=driver.find_element_by_id('password')
b.send_keys('User@1234')
captcha=input()
c=driver.find_element_by_id('captchaimg')
c.send_keys(captcha)
# d=driver.find_element(by=By.NAME,value='button')
d=driver.find_element_by_name('button')
d.click()
otp=input()
a=driver.find_element(by='name',value='otp')
a.send_keys(otp)
driver.find_element(By.TAG_NAME,'button').click()
driver.get('https://videshapps.gov.in/videsh/apar/view_apar')
# driver.implicitly_wait(5)
# WebDriverWait(driver,10).until(
#     # EC.text_to_be_present_in_element(By.CLASS_NAME,'btn btn-warning btn-sm'),'View'
#     EC.element_to_be_clickable((By.NAME,'btnsave'))
# )
# wait = 
# alert=wait.until(EC.alert_is_present())
# alert.accept()
# b=driver.find_element(By.CLASS_NAME,'btn btn-warning btn-sm')
# document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
# b.click()
WebDriverWait(driver,2)

driver.execute_script("a=document.querySelector(\"body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a\");a.click();")
# document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar.closed-sidebar-mobile.closed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
WebDriverWait(driver,4)
all_els=driver.find_elements(By.TAG_NAME,'button')
el=None
grade=
for i in all_els:
    if i.text=='Approve Apar':
        print
        el=i
el.click()
# c=driver.find_element(By.CLASS_NAME,"btn btn-primary btn-sm")
# c.click()
driver.execute_script("a=document.querySelector(\"#num_box\");a.innerHTML=110030")
WebDriverWait(driver,4).until(
    EC.text_to_be_present_in_element((By.ID,'gen_sign'),'Verify Pin')
)
try:
    e=driver.find_element(By.ID,'gen_sign')
    e.click()
except:
    print('dasdsa')


wait = WebDriverWait(driver, 10)
alert=wait.until(EC.alert_is_present())
alert.accept()
driver.get('https://videshapps.gov.in/videsh/apar/view_apar')
# document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar.closed-sidebar-mobile.closed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
# b=driver.find_elements(By.TAG_NAME,'a')
# for i in b:
#     print(i.text)
# link=b[1]