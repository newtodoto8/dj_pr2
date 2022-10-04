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
import os
import datetime

def fn(dt1,dt2):
	months = {	'01':'January',
		'02':'February',
		'03':'March',
		'04':'April',
		'05':'May',
		'06':'June',
		'07':'July',
		'08':'August',
		'09':'September',
		'10':'October',
		'11':'November',
		'12':'December'		}
	months=dict((x,y) for y,x in months.items())
	day,month,year=dt1.split()
	day2,month2,year2=dt2.split()
	month,month2=months[month],months[month2]
	print(day2,month2,year2)
	day,month,year=map(int,[day,month,year])
	day2,month2,year2=map(int,[day2,month2,year2])
	diff=datetime.date(year2,month2,day2)-datetime.date(year,month,day)
	print(diff.days)
	return diff.days


v=r"C:\Users\user\Documents\garbage\python\selenium\chromedriver_win32"
os.environ['PATH']+=os.path.abspath(v)
driver = webdriver.Chrome()
base='https://videshapps.gov.in/videsh/apar/view_nrp/'
driver.get(base)
a=driver.find_element_by_id('email')
a.send_keys('vcrsection@mea.gov.in')
b=driver.find_element_by_id('password')
b.send_keys('User@1234')
x=input()
driver.find_element(By.ID,'captchaimg').send_keys(x)
d=driver.find_element_by_name('button')
d.click()
e=driver.find_elements(By.TAG_NAME,'form')
f=driver.find_element(by='name',value='otp')
otp=input()
f.send_keys(otp)
driver.find_element(By.TAG_NAME,'button').click()
for i in range(102,104):
	page_no=i*20
	page_urls=''
	if page_no==0:
		page_urls=''
	else:
		page_urls=str(page_no)
	total_url=base+page_urls
	driver.get(total_url)
	
	all_tds=driver.find_elements(By.TAG_NAME,'td')
	Counter=True
	cc=0
	
		
	while(cc<len(all_tds)):
		WebDriverWait(driver,2)
		driver.get(total_url)
		all_tds=driver.find_elements(By.TAG_NAME,'td')
		while cc<len(all_tds) and all_tds[cc].text!='Pending':
			cc+=1
		if cc>=len(all_tds):
			continue
		if all_tds[cc].text=='Pending':
			link=all_tds[cc+1]
			link.click()
			start_date=None
			end_date=None
			tds=driver.find_elements(By.TAG_NAME,'td')
			for m,k in enumerate(tds):
				if k.text=='NRP from':
					start_date=tds[m+1].text
				if k.text=='NRP to':
					end_date=tds[m+1].text
			diff=fn(start_date,end_date)
			if diff>90:
				tds_in=driver.find_elements(By.TAG_NAME,'td')
				print(tds_in[1].text,tds_in[3].text,'\n')
				print('greater than 90 days\n')
				cc+=1
				continue
			else:
				print('\n')
				tds_in=driver.find_elements(By.TAG_NAME,'td')
				print(tds_in[1].text,tds_in[3].text,'\n')
				all_links=driver.find_elements(By.TAG_NAME,'a')
				cc+=1
				for l in all_links:
					if l.text=='Take Action':
						l.click()
						break

				driver.execute_script('let a=document.getElementsByName(\'action\')[0];a.value=\'1\';var b=document.getElementsByName(\'remark\')[0];b.innerHTML=\'Less than 90 days\';var c=document.getElementById(\'btnsave\');c.click();')
		


