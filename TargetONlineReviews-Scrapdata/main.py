import time
from datetime import datetime, timedelta
import xlsxwriter
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
import pandas as pd
# import xlsxwriter
# from xlrd import open_workbook
import openpyxl
import os.path

# extraction from excel dataset
pth = (str(Path.cwd()) + '\DPCI Helping File With Tab Information.xlsx')
print(pth)
df = pd.read_excel(pth, sheet_name='Final Sheet')
df1 = df.loc[:,
      ["DPCI 1", "Enable"]]
print(df1)

df2 = df1[~df1["Enable"].isnull()]
print(df2)

# variables
lstTitles = []
lstReview = []
# set browser launch options
options = Options()
options.add_argument("start-maximized")
# set browser launch options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# loop on excel dataset
for index, row in df2.iterrows():
    dpci = row['DPCI 1']
    print(dpci)

    # navigate to the target page
    driver.get('https://www.target.com/s?searchTerm=' + dpci)
    time.sleep(5)
    for glink in driver.find_elements(by=By.CLASS_NAME, value='cWxnyu a[href]'):
        glink.click()
        continue

    time.sleep(10)
    loadMoreFound = "Yes"
    while loadMoreFound == "Yes":
        loadMoreFound = "No"
        try:
            for loadmore in driver.find_elements(by=By.CLASS_NAME, value='gcGvjK'):
                t = loadmore.text
                if "Load" in t:
                    loadMoreFound = "Yes"
                    loadmore.click()
                    time.sleep(2)
                    break
        except:
            print("Error")
            loadMoreFound = "No"
    counter = 0
    # Title
    for ReviewTitle in driver.find_elements(by=By.CLASS_NAME, value='eJeHYp h3'):
        t = ReviewTitle.text
        lstTitles.append(t)
        print(t)
    # User time review
    for Reviewdetail in driver.find_elements(by=By.CLASS_NAME, value='zhyqn,h-text-sm span'):
        if "Would" in Reviewdetail.text:
            counter += 1
            t = Reviewdetail.text.splitlines()
            t.insert(0, lstTitles[counter])
            rate = t[1][0]  # first charactor of rating
            t[1] = rate
            ulist = t[3].split('-')
            t[3] = ulist[0]
            # date time setting
            if 'year' in ulist[1]:
                y1 = ulist[1].strip()
                y = int(y1[0])
                y = y * 365
                t.insert(4, str(datetime.today() - timedelta(days=y)))
            if 'month' in ulist[1]:
                y1=ulist[1].strip()
                y = int(y1[0])
                y = y * 30
                t.insert(4, str(datetime.today() - timedelta(days=y)))
            if 'day' in ulist[1]:
                y1 = ulist[1].strip()
                y = int(y1[0])
                t.insert(4, str(datetime.today() - timedelta(days=y)))
            lstReview.append(t)

    df = pd.DataFrame(lstReview)
    writer = pd.ExcelWriter(dpci.xlsx, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Data', index=False)
    writer.save()
    print(lstReview)

input("exit\n")

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
