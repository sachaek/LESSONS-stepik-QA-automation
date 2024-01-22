import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
# time.sleep(3)
button = browser.find_element(By.ID, "verify")
button.click()
# time.sleep(3)
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text