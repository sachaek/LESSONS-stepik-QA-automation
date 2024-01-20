import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

browser = webdriver.Chrome()


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get("https://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

    submit = browser.find_element(By.CLASS_NAME, "btn-default")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()