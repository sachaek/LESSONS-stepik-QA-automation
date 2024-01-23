from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By


def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    input1.send_keys("Alex")
    input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    input2.send_keys("Surname")
    input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
    input3.send_keys("sacha@mail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Поздравляем! Вы успешно зарегистировались!", "registration is failed")


if __name__ == "__main__":
    unittest.main()