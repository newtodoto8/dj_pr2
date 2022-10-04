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