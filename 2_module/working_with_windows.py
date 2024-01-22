import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get("https://suninjuly.github.io/alert_accept.html")

    button1 = browser.find_element(By.CLASS_NAME, "btn-primary")
    button1.click()
    confirm1 = browser.switch_to.alert
    confirm1.accept()
    time.sleep(2)

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer1 = browser.find_element(By.ID, "answer")
    answer1.send_keys(y)

    submit1 = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit1.click()

finally:
    time.sleep(10)
    browser.quit()