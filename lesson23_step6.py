import time
import os
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"


with webdriver.Chrome() as browser:
    browser.get(link)

    browser.find_element_by_css_selector('button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(10)
