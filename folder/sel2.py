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
from selenium.webdriver.support.select import Select
# from selenium import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# service = Service(executable_path=ChromeDriverManager().install())
import os
v=r"C:\Users\user\Documents\garbage\python\selenium\chromedriver_win32"
os.environ['PATH']+=os.path.abspath(v)

driver = webdriver.Chrome()
counter=0
driver.get('http://10.197.207.8/videsh/apar/view_apar/60')
a=driver.find_element_by_id('email')
a.send_keys('vcrsection@mea.gov.in')
b=driver.find_element_by_id('password')
b.send_keys('123')
x=input()
driver.find_element(By.ID,'captchaimg').send_keys(x)
d=driver.find_element_by_name('button')
d.click()
e=driver.find_elements(By.TAG_NAME,'form')
f=driver.find_element(by='name',value='otp')
f.send_keys(e[0].text)
g=driver.get('http://10.197.207.8/videsh/apar/view_apar/60')
els=driver.find_elements(By.TAG_NAME,'a')
length_els=len(els)
while (counter<length_els):
    WebDriverWait(driver,2)
    driver.get('http://10.197.207.8/videsh/apar/view_apar/60')
    # wait = WebDriverWait(driver, 10)
    # alert=wait.until(EC.alert_is_present())
    # alert.accept()
    # b=driver.find_element(By.CLASS_NAME,'btn btn-warning btn-sm')
    # document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
    # b.click()
    els=driver.find_elements(By.TAG_NAME,'a')
    # refs=[]
    # print([i.text for i in els])
    while els[counter].text!='View':
        counter+=1
    # driver.get('http://10.197.207.8/videsh/apar/view_apar')
    if els[counter].text=='View':
        
        els[counter].click()
        # driver.execute_script("a=document.querySelector(\"body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar.closed-sidebar-mobile.closed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a\");a.click();")

    # document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar.closed-sidebar-mobile.closed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
        WebDriverWait(driver,4)
        grade={'PA':['No','No','No','No','Yes'],'PPS':['No','No','No','Yes','Yes'],'ASO':['No','No','No','No','No','Yes','Yes'],'MTS':['No','No','No','No','No','No','No']}
        def mapping(x):
            if 8<=x<=10:
                return 8
            elif 6<=x<=7.99:
                return 6
            elif 4<=x<=5.99:
                return 4
            else:
                return 0
        gr=driver.find_elements(By.TAG_NAME,'td')
        gr=gr[1].text
        rem_list=driver.find_elements(By.NAME,'remark_ro[]')
        ch=None
        if gr=='FOR GRADE - PS' or gr=='FOR GRADE - PA' or gr=='FOR GRADE - Steno':
            ch=grade['PA']
        elif gr=='FOR GRADE - PPS' or gr=='FOR GRADE - Sr PPS':
            ch=grade['PPS']
        elif gr=='FOR GRADE - Section Officer' or gr=='FOR GRADE - Assistant Section Officer' or gr=='FOR GRADE - JSA' or gr=='FOR GRADE - SSA':
            ch=grade['ASO']
        elif gr=='FOR GRADE CHAUFFEUR AND DISPATCH RIDER' or gr=='FOR GRADE MULTI-TASKING STAFF':
            ch=grade['MTS']
        if gr=='FOR GRADE - Section Officer' or gr=='FOR GRADE - Assistant Section Officer' or gr=='FOR GRADE - JSA' or gr=='FOR GRADE - SSA':
            all_tds=driver.find_elements(By.TAG_NAME,'td')
            ro_score=None
            rvo_score=None
            for n,td in enumerate(all_tds):
                if td.text=='Total Sum:':
                    ro_score=all_tds[n+1].text
                    rvo_score=all_tds[n+2].text
                    break

            if (mapping(int(ro_score))==mapping(int(rvo_score))):
                pass
            else:
                counter+=1
                continue
        #     agree_ro=driver.find_element(By.ID,'agree_to_ro')
        #     agree=Select(agree)
        #     agree=agree.all_selected_options
        #     for i in agree:
        #         if i.text=='Yes'
        flag=False    
        for n,rem in enumerate(rem_list):
            xx=Select(rem)
            xx = xx.all_selected_options
            for i in xx:
                if i.text==ch[n]:
                    continue
                else:
                    # driver.get('file:///C:/Users/user/Documents/garbage/python/selenium/test_site/index.html')
                    flag=True
                    break


        if flag:
            counter+=1
            continue
        if gr!='FOR GRADE CHAUFFEUR AND DISPATCH RIDER' and gr!='FOR GRADE MULTI-TASKING STAFF':
            RO=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div/div/div[4]/table[3]/tbody/tr[1]/td[1]')
            RvO=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div/div/div[4]/table[3]/tbody/tr[2]/td[1]')
            if RO.text==RvO.text:
                counter+=1
                continue

        all_els=driver.find_elements(By.TAG_NAME,'button')
        el=None
        for i in all_els:
            if i.text=='Approve Apar':
                print
                el=i
        el.click()
        # c=driver.find_element(By.CLASS_NAME,"btn btn-primary btn-sm")
        # c.click()
        driver.execute_script("a=document.querySelector(\"#num_box\");a.innerHTML=123456")
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
        WebDriverWait(driver,2)
        # counter+=1


browser.quit()
    
# document.querySelector("body > div.app-container.app-theme-white.body-tabs-shadow.fixed-header.fixed-sidebar.closed-sidebar-mobile.closed-sidebar > div.app-main > div > div > div > div.col-md-12.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(9) > a")
# b=driver.find_elements(By.TAG_NAME,'a')
# for i in b:
#     print(i.text)
# link=b[1]