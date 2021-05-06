import time
import math

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"


with webdriver.Chrome() as browser:
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    result = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(result)

    input2 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
    input2.click()

    input3 = browser.find_element_by_id("robotsRule")
    input3.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

    time.sleep(10)
