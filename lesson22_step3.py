import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"


with webdriver.Chrome() as browser:
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(int(num1)+int(num2)))

    button = browser.find_element_by_css_selector("button")
    button.click()

    time.sleep(10)
