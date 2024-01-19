from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

in_link = "https://www.degreesymbol.net/"
browser = webdriver.Chrome()

try:
    browser.get(in_link)
    link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    link.click()

finally:
    time.sleep(3)
    browser.quit()