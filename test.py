from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from ckonlpy.tag import Twitter
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display


display = Display(visible=0, size=(1024, 768))
display.start()

options = Options()
options.binary_location = "/usr/bin/google-chrome"

# chrome_options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')

# chrome = webdriver.Chrome(executable_path=self.driver_path, options=options)

chrome = webdriver.Chrome(executable_path="static/lib/webDriver/chromedriver_linux")
chrome.implicitly_wait(30)

keyword='마이삭'
url = 'https://twitter.com/search?q={}&src=typed_query'.format(keyword)
chrome.get(url)
chrome.implicitly_wait(30)

body = chrome.find_element_by_css_selector('body')
#text2 = chrome.find_elements_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div')
#text2 = chrome.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div')

result = []

for i in range(10):
    for q in range(2):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    text2 = chrome.find_elements_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > section > div')
    result.append(re.sub('\n', '', text2[0].text))

time.sleep(1)
# if self.platform == 'linux':
#     chrome.close()

t = Twitter()

# t.add_dictionary(self.sajun(), 'Noun')
print('단어사전 추출완료')
tokens_ko = []

for i in range(len(result)):
    tokens_ko.append(t.nouns(result[i]))

final = []
for _, q in enumerate(tokens_ko):
    for i in range(len(q)):
        final.insert(-1, q[i])
print(final[0])
