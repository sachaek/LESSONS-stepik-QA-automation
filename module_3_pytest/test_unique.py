from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestUniqueSelectors(unittest.TestCase):
    def test_registration_1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Alex")
            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Surname")
            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("sacha@mail.com")
            time.sleep(1)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text
            original_text = "Congratulations! You have successfully registered!"
            error_message = f"first test failed, original text == {original_text}, output text == {welcome_text}"
            self.assertEqual(original_text, welcome_text, error_message)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_registration_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
            input1.send_keys("Alex")
            input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
            input2.send_keys("Surname")
            input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
            input3.send_keys("sacha@mail.com")
            time.sleep(1)
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text
            original_text = "Congratulations! You have successfully registered!"
            error_message = f"first test failed, original text == {original_text}, output text == {welcome_text}"
            self.assertEqual(original_text, welcome_text, error_message)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()