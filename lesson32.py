from selenium import webdriver
import time
import unittest


link1 = "http://suninjuly.github.io/registration1.html"    # Ссылка на успешное прохождение
link2 = "http://suninjuly.github.io/registration2.html"      # Ссылка на неуспешное прохождение


def get_links(link):
    with webdriver.Chrome() as browser:
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".first_block .third")
        input3.send_keys("Smolensk")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
    return welcome_text


class TestLinks(unittest.TestCase):

    def test_link1(self):
        self.assertEqual(get_links(link1), "Congratulations! You have successfully registered!")

    def test_link2(self):
        self.assertEqual(get_links(link2), "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
