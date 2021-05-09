import pytest
import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_shopcart_available(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(2)
    assert not browser.findElements(By.CLASS_NAME("btn-primary")).isEmpty()
