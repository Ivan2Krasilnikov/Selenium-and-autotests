from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/find_link_text'


with webdriver.Chrome() as browser:
    browser.get(link)
    desired_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link = browser.find_element_by_partial_link_text(desired_text)
    link.click()

    value1 = "input"
    value2 = "last_name"
    value3 = "city"
    value4 = "country"

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(30)

