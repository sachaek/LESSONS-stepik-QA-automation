import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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


@pytest.mark.parametrize('link', list_of_pages[0:1])
@pytest.fixture(scope="class")
def browser(link):
    browser = webdriver.Chrome()
    print('\nbrowser start')
    browser.implicitly_wait(10)
    browser.get(link)
    yield browser
    print('\nbrowser quit')
    browser.quit()


class TestLogin:
    def test_button_sign(self, browser):
        button = browser.find_element(By.ID, "ember33")
        button.click()

    def test_sign_form(self, browser):
        input2 = browser.find_element(By.ID, "id_login_email")
        input2.send_keys("email")
        input3 = browser.find_element(By.ID, "id_login_password")
        input3.send_keys("password")
        button = browser.find_element(By.CLASS_NAME, "sign-form__btn")
        button.click()
        print('shaulin')

    @pytest.mark.xfail()
    def test_button_sign_failed(self, browser):
        button = WebDriverWait(browser, 5).until(
             EC.element_to_be_clickable((By.ID, "ember33"))
            )
        # button = WebDriverWait(browser, 3).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        # )
        # button = browser.find_element((By.ID, "ember33"))
        button.click()
