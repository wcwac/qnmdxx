from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

cookies = eval(os.environ["cookies"])
url = os.environ["url"]

option = webdriver.ChromeOptions()
option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat"')
option.add_argument('--disable-infobars')
option.add_argument("--disable-extensions")
option.add_argument("--disable-gpu")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--no-sandbox")
option.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=option)
driver.set_window_size(640 , 960)
driver.get(url + '/icon/icon.png')
driver.delete_all_cookies()

for i in cookies:
    driver.add_cookie({'name':i,'value':cookies[i],'path':'/'})

delay=5

def studyArticle(i):
    driver.get(url + '/study/studyList')
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="study"]/div[1]/div[1]/div/div[2]/span').click()
    time.sleep(delay)
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="study"]/div[2]/div/div[2]/li[{}]/div[2]'.format(i)).click()
    time.sleep(delay)

def checkIn():
    driver.get(url + '/study/personalSet')
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="peopleset"]/div[1]/div[2]/button').click()
    time.sleep(delay)


def studyMovie():
    driver.get(url + '/study/studyList')
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="study"]/div[2]/div/div[2]/li[1]/div[2]').click()
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@id="home"]/div/div[3]/button').click()
    time.sleep(delay)

def getScore():
    driver.get(url + '/study/personalSet')
    time.sleep(delay)
    return driver.find_element_by_xpath('//*[@id="peopleset"]/div[2]/div[2]/div[2]/p[2]').text

checkIn()
print(getScore())
studyMovie()
print(getScore())
for i in range(1,5):
    studyArticle(i)
print(getScore())
