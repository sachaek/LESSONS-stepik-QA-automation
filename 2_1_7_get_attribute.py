from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is selected by default"
    people_radio = browser.find_element(By.ID, "robotsRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is None, "Robots is not selected by default"

finally:
    pass