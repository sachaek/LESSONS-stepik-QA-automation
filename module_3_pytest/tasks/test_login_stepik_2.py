import math
import time

import pytest
from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    print('\nbrowser start')
    browser.implicitly_wait(10)
    yield browser
    print('\nbrowser quit')
    browser.quit()


class TestLogin:
    list_of_pages = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]
    string_for_message = ""

    @pytest.mark.parametrize('link', list_of_pages[3:])
    def test_button_sign(self, browser, link):
        browser.get(link)
        button_login = browser.find_element(By.ID, "ember33")
        button_login.click()

        input2 = browser.find_element(By.ID, "id_login_email")
        input2.send_keys("email")
        input3 = browser.find_element(By.ID, "id_login_password")
        input3.send_keys("password")
        button_submit_login = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        button_submit_login.click()
        print('1111111')

        time.sleep(1)
        elements = browser.find_elements(By.CSS_SELECTOR, ".again-btn")
        if elements:
            elements[0].click()
        time.sleep(1)
        picker_textarea = (By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...'")
        textarea = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(picker_textarea))
        time.sleep(1)
        textarea.send_keys(str(math.log(int(time.time()-1.4))))
        print('1111111')
        button1 = WebDriverWait(browser, 10).until(
             EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
            )
        button1.click()
        print('1111111')
        assert True

