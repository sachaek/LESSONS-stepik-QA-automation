import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

"""
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# найдет элемент button, проскроллит до тех пор когда элемент окажется вверху
"""

def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    input3 = browser.find_element(By.ID, "answer")
    input3.send_keys(answer)

    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 75);")
    # Эта команда проскроллит страницу на 100 пикселей вниз

    input1 = browser.find_element(By.ID, "robotCheckbox")
    input1.click()

    input2 = browser.find_element(By.ID, "robotsRule")
    input2.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()




finally:
    time.sleep(7)
    browser.quit()
