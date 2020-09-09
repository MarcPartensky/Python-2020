#!.usr/bin/env python
import os
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = 'https://portail.isep.fr/'
ISEP_PASSWORD = os.environ["ISEP_PASSWORD"]
ISEP_ID = os.environ["ISEP_ID"]

driver.get(url)
elements = driver.find_elements_by_tag_name('input')
isep_id, isep_password = elements[3:5]
isep_id.click()
isep_id.send_keys(ISEP_ID)
isep_password.click()
isep_password.send_keys(ISEP_PASSWORD)
submit_buttons = driver.find_elements_by_tag_name('button')
submit = submit_buttons[0]
submit.click()
