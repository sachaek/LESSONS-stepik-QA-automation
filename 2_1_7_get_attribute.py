import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get("https://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.ID, "treasure")
    valuex = treasure.get_attribute("valuex")

    y = calc(valuex)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    submit = browser.find_element(By.CLASS_NAME, "btn-default")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()

