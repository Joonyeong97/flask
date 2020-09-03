# import pymysql
# import datetime
# current = datetime.datetime.now()
# nine_hour_later = current + datetime.timedelta(hours=9)
# date = nine_hour_later.strftime("%Y%m%d")

from selenium import webdriver
import time
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

PATH = 'static/lib/webDriver/chromedriver_linux'
chrome = webdriver.Chrome(executable_path=PATH, options=options)

chrome.implicitly_wait(30)

url = 'http://www.data-cook.com/crawl'
chrome.get(url)
chrome.implicitly_wait(30)

elm = chrome.find_element_by_id('crawl')
elm.send_keys('1542AA')

elm = chrome.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/button')
time.sleep(1)
elm.click()

time.sleep(1)
chrome.close()