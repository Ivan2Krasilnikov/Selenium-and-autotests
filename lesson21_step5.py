from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    input3 = browser.find_element_by_id("robotsRule")
    input3.click()

    button = browser.find_element_by_css_selector("button")
    button.click()

    time.sleep(10)
