import time


def test_add_to_basket_btn(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_basket_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    time.sleep(8)
    assert add_to_basket_btn.is_displayed(), "Add to basket button is not displayed"
