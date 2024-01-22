import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()


try:
    browser.get("https://suninjuly.github.io/selects2.html")
    a = int(browser.find_element(By.ID, "num1").text)
    b = int(browser.find_element(By.ID, "num2").text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(a+b))

    button1 = browser.find_element(By.CLASS_NAME, "btn-default")
    button1.click()

finally:
    time.sleep(3)
    browser.quit()
