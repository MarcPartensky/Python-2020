from selenium import webdriver
import json
import os
import time

driver = webdriver.Chrome()

driver.get('https://leekwars.com/')

driver.get('https://leekwars.com/login')
time.sleep(3)
login_xpath = '//*[@id="app"]/div/div[4]/div/div[2]/div/div/div/div/form/input[1]'
login_button = driver.find_element_by_xpath(login_xpath)
login_button.send_keys(os.environ['LEEKWARS_USERNAME'])
time.sleep(1)
password_xpath = '//*[@id="app"]/div/div[4]/div/div[2]/div/div/div/div/form/input[2]'
password_button = driver.find_element_by_xpath(password_xpath)
print(password_button)
password_button.send_keys(os.environ['LEEKWARS_PASSWORD'])
time.sleep(1)
submit_xpath = '//*[@id="app"]/div/div[4]/div/div[2]/div/div/div/div/form/center/button'
submit_button = driver.find_element_by_xpath(submit_xpath)
submit_button.submit()
time.sleep(1)
driver.get("https://leekwars.com/api/garden/get-leek-opponents/69649")
r = json.loads(driver.find_element_by_tag_name('body').text)
print(r)
