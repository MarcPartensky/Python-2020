#!/usr/bin/env python
import os
import time

from selenium import webdriver

ISEP_PASSWORD = os.environ["ISEP_PORTAL_PASSWORD"]
ISEP_ID = os.environ["ISEP_ID"]

url = 'https://portail.isep.fr/'
driver = webdriver.Chrome('./chromedriver')

driver.get(url)
time.sleep(1)
elements = driver.find_elements_by_tag_name('input')
isep_id = driver.find_element_by_id('userfield')
isep_password = driver.find_element_by_id('passwordfield')
isep_id.click()
isep_id.send_keys(ISEP_ID)
isep_password.click()
isep_password.send_keys(ISEP_PASSWORD)
submit_buttons = driver.find_elements_by_tag_name('button')
submit = submit_buttons[0]
submit.click()


