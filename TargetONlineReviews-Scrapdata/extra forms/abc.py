from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set browser launch options
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
driver.implicitly_wait(10)
driver.get(url)
driver.implicitly_wait(10)
for quote in driver.find_elements(by=By.CLASS_NAME, value='quote'):
    print(quote.text)



input('Press ENTER to close the automated browser')
driver.quit()


'''import requests
url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
my_cookies = {
'nonce': '2315',
'PHPSESSID': 'rtc4l3m3bgmjo2fqmi0og4nv24'
}
r = requests.get(url + 'quotes.php', params={'p': '0'}, cookies=my_cookies)
print(r.text)
'''
'''import requests
url = 'http://www.webscrapingfordatascience.com/simplejavascript/quotes.php'
#url='https://www.target.com/s?searchTerm=025-03-6944'
# Note that cookie values need to be provided as strings
r = requests.get(url, cookies={'jsenabled': '1'})
print(r.json())'''



'''import requests
from bs4 import BeautifulSoup
url = 'http://www.webscrapingfordatascience.com/simplejavascript/'
url = 'https://www.target.com/s?searchTerm=025-03-6944'
r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')
# No tag will be found here
ul_tag = html_soup.find('ul')
print(ul_tag)
# Show the JavaScript code
script_tag = html_soup.find('script', attrs={'src': None})
print(script_tag)'''