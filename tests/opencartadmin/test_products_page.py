from pages.locators import AdminAddProductPage
from pages.locators import AdminLoginPageLocators
from pages.locators import AdminProductsPage
from selenium.webdriver.common.keys import Keys
import time


def authorization(browser):
    username = browser.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
    username.send_keys("admin")
    password = browser.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
    password.send_keys("admin")
    password.send_keys(Keys.ENTER)


def test_add_new_product(browser, base_url):
    browser.get(base_url + '/opencart/admin/index.php?route=catalog/product&user_token=w2lFNch22HwgP9i00euVDJteZjFt1HyB')
    authorization(browser)
    browser.find_element(*AdminProductsPage.ADD_NEW_BUTTON).click()
    product_name = browser.find_element(*AdminAddProductPage.PRODUCT_NAME_INPUT)
    product_name.send_keys("Tesla")
    product_name_text = product_name.get_attribute("value")
    meta_tag_title = browser.find_element(*AdminAddProductPage.META_TAG_TITLE_INPUT)
    meta_tag_title.send_keys("mytesla")
    browser.find_element(*AdminAddProductPage.DATA_TAB).click()
    model = browser.find_element(*AdminAddProductPage.MODEL_INPUT)
    model.send_keys("Model Y")
    price = browser.find_element(*AdminAddProductPage.PRICE_INPUT)
    price.clear()
    price.send_keys("1000000")
    quantity = browser.find_element(*AdminAddProductPage.QUANTITY_INPUT)
    quantity.clear()
    quantity.send_keys("5")
    browser.find_element(*AdminAddProductPage.SAVE_BTN).click()

    products = browser.find_elements(*AdminProductsPage.RANDOM_PRODUCT_NAME)
    flag = False
    for pr in products:
        if pr.text == product_name_text:
            flag = True
            break

    assert flag
