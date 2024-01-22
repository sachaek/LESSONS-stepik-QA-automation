import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()


def calc(x: str) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    value = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    value_x = browser.find_element(By.ID, "input_value").text
    y = calc(value_x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(7)
    browser.quit()