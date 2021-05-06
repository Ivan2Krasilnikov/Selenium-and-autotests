import time
import os

from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"


with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Name')

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('LastName')

    input3 = browser.find_element_by_name('email')
    input3.send_keys('email@.com')

    input4 = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'sel.txt')
    input4.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(10)
