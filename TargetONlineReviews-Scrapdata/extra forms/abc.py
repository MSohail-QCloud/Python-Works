

import requests
url = 'http://www.webscrapingfordatascience.com/simplejavascript/quotes.php'
#url='https://www.target.com/s?searchTerm=025-03-6944'
# Note that cookie values need to be provided as strings
r = requests.get(url, cookies={'jsenabled': '1'})
print(r.json())



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