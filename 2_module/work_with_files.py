import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


try:
    browser.get("https://suninjuly.github.io/file_input.html")

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    input1.send_keys("Alexender")

    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    input2.send_keys("SMITH")

    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    input3.send_keys("sa@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    input4 = browser.find_element(By.CSS_SELECTOR, "input[id='file']")
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()