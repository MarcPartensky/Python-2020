"""Find locations in issy-les-moulineaux and keep me informed of new offers."""
import os

from selenium import webdriver

URL = "https://logement.isep.fr/"
URL_SORTED_BY_CHEAPEST = "https://logement.isep.fr/listelogement.php?tri=n|loyer"

driver = webdriver.Chrome()
driver.get(URL)

id_value, password_value = os.environ['ISEP_ID'], os.environ['ISEP_PASSWORD']
id_field, password_field, submit_field = driver.find_elements_by_tag_name('input')

id_field.click()
id_field.send_keys(id_value)

password_field.click()
password_field.send_keys(password_value)

submit_field.click()


driver.get(URL_SORTED_BY_CHEAPEST)
