from selenium import webdriver
import time


# link = "http://suninjuly.github.io/registration1.html"    # Ссылка на успешное прохождение
link = "http://suninjuly.github.io/registration2.html"      # Ссылка на неуспешное прохождение

with webdriver.Chrome() as browser:
    browser.get(link)

    value1 = "div.first_block input.first"
    value2 = "div.first_block input.second"
    value3 = "div.first_block input.third"

    input1 = browser.find_element_by_css_selector(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(value3)
    input3.send_keys("Smolensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    time.sleep(10)
