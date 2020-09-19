#!.usr/bin/env python
import os
import time

from selenium import webdriver

ISEP_PASSWORD = os.environ["ISEP_HYPERPLANNING_PASSWORD"]
ISEP_ID = os.environ["ISEP_ID"]

url = 'https://planning-2021.isep.fr/etudiant'
driver = webdriver.Chrome('./chromedriver')

driver.get(url)
time.sleep(1)

isep_id = driver.find_element_by_id('GInterface.Instances[0].Instances[0].idIdentification.bouton_Edit')
isep_id.click()
isep_id.send_keys(ISEP_ID)


isep_password = driver.find_element_by_id('GInterface.Instances[0].Instances[0]_password')
isep_password.click()
isep_password.send_keys(ISEP_PASSWORD)

connect_button = driver.find_element_by_id('GInterface.Instances[0].Instances[0].idBtnConnexion')
connect_button.click()

time.sleep(2)

lesson_button = driver.find_element_by_id('GInterface.Instances[0].Instances[0]_Liste_niveau0')
lesson_button.click()
