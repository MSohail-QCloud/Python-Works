import time
import urllib.request
import zipfile
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# set browser launch options
options = Options()
options.add_argument("start-maximized")

# set browser launch options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
dpci = '025-03-6944'
time.sleep(5)

# Set an implicit wait
#driver.implicitly_wait(10)

# navigate to the target page
driver.get('https://www.target.com/s?searchTerm=' + dpci)
for i in range(100):
    print(driver.find_elements(By.CSS_SELECTOR, '.h-display-flex a[href]')[i])
#driver.find_elements(By.CSS_SELECTOR, '.h-display-flex a[href]')[2].click()
input("exit")
'''


quote_elements = WebDriverWait(browser, 10).until(
EC.presence_of_all_elements_located(
(By.CSS_SELECTOR, ".h-display-flex a[href]")
)
)
for quote in quote_elements:
    print(quote.text)
input('Press ENTER to close the automated browser')





time.sleep(5)
browser.find_elements(By.CSS_SELECTOR('.h-display-flex a[href]'))
# fill register form
#browser.find_element_by_name('email').send_keys('orlojva22uqey9@bc.ru')
#time.sleep(5)
input(" enter key to exit")
'''
