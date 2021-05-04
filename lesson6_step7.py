from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = 'http://suninjuly.github.io/huge_form.html'


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)

