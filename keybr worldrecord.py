from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyautogui
import time

driver = webdriver.Chrome()

driver.get('https://www.keybr.com/multiplayer')

while True:
    ticker = driver.find_element_by_class_name('Ticker')
    if ticker.text == "GO!":
        break

inp  = driver.find_element_by_class_name('TextInput-fragment')

text = driver.find_element_by_xpath("//*[@type='text']")
print(text.send_keys('salut'))
time.sleep(1)
for e in inp.find_elements_by_tag_name('span'):
    print(e)
    if e.text=='␣':
        pyautogui.press(' ')
    elif e.text=='↵':
        pyautogui.press('enter')
    else:
        pyautogui.press(e.text)
    time.sleep(0.01)
