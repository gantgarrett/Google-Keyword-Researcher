from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle
import time

chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://curiouscat.me/communities/2/question_exchange')

timechanger = driver.find_element_by_xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[5]/a')
timechanger.click()
#access_button = driver.find_element_by_xpath(('//*[@id="app"]/div[1]/div[1]/div/button'))
#access_button.click()

#twitter_button = driver.find_element_by_xpath(('//*[@id="app"]/div[1]/div[3]/div[4]/div/div/div/div/p[1]'))
#twitter_button.click()


