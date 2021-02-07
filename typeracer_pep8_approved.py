from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://play.typeracer.com/"
driver = webdriver.Chrome()
driver.get(url)
try:
    agree = driver.find_element_by_xpath("//button[text()='Agree']")
    agree.click()
except:
    time.sleep(2)
    accept = driver.find_element_by_xpath(
        "//button[normalize-space()='I accept']")
    accept.click()
time.sleep(3)
racefriends = driver.find_element_by_xpath("//a[text()='Race your friends']")
racefriends.click()

time.sleep(1)
closepopup = driver.find_element_by_xpath("//a[text()='OK']")
closepopup.click()

joinracebtn = driver.find_element_by_xpath("//a[text()='join race »']")
joinracebtn.click()

time.sleep(2)

waiting = True
while waiting:
    elements = driver.find_elements_by_xpath(
        "//div[text()='Waiting for competitors...']"
    )
    waiting = bool(elements)

time.sleep(2)

waiting = True
while waiting:
    countdowns = driver.find_elements_by_css_selector(
        "body > div.countdownPopup.horizontalCountdownPopup > div > table > tbody > tr > td > table > tbody > tr > td:nth-child(1)"
    )
    waiting = bool(countdowns)

time.sleep(1)
textspans = driver.find_element_by_xpath(
    '//*[@id="gwt-uid-17"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div'
)

spans = textspans.find_elements_by_tag_name("span")
spans = [span.text for span in spans]

print(spans)

text = " ".join(spans)
text = text.replace(" ", "", 1)
text += Keys.ENTER

print(text)

txtinput = driver.find_element_by_class_name("txtInput")

txtinput.send_keys(text)
