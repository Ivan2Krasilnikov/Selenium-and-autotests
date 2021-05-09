import pytest
import time
import math
from selenium import webdriver


urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', urls)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(2)
    input_box = browser.find_element_by_tag_name('textarea')
    answer = math.log(int(time.time()))
    input_box.send_keys(str(answer))

    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()

    browser.implicitly_wait(2)

    feedback = browser.find_element_by_css_selector('.smart-hints__hint').text

    assert feedback == "Correct!", f'Ожидался ответ "Correct!", получил "{feedback}"'
