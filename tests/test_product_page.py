import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators


def test_product_page(browser, base_url):
    """
    Dz9. Just finding of elements on the product page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    browser.get(base_url + '/opencart/index.php?route=product/product&product_id=40')
    browser.find_element(*ProductPageLocators.THUMBNAILS)
    browser.find_element(*ProductPageLocators.DESC_AND_REVIEW_TABS)
    browser.find_element(*ProductPageLocators.TAB_CONTENT)
    browser.find_element(*ProductPageLocators.QUANTITY_INPUT)
    browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
    browser.find_element(*ProductPageLocators.RATING)


def test_send_review(browser, base_url):
    """
    dz10. Sends review about product and checks if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    browser.get(base_url + '/opencart/index.php?route=product/product&product_id=40')
    explicit_wait = WebDriverWait(browser, 5)
    review_tab = browser.find_element(*ProductPageLocators.REVIEW_TAB)
    review_tab.click()
    review_name_input = explicit_wait.until(
        EC.visibility_of_element_located(ProductPageLocators.REVIEW_NAME_INPUT)
    )
    review_name_input.send_keys("Name")
    review_text_input = explicit_wait.until(
        EC.visibility_of_element_located(ProductPageLocators.REVIEW_TEXT_INPUT)
    )
    review_text_input.send_keys("This is my first review ever")
    rating = random.randint(0, 4)
    review_rating = browser.find_elements(*ProductPageLocators.REVIEW_RATING_MARKS)[rating]
    review_rating.click()
    browser.find_element(*ProductPageLocators.REVIEW_BTN).click()
    alert = browser.find_elements(*ProductPageLocators.ALERTS)[0]

    assert alert.text == "Thank you for your review." \
                         "It has been submitted to the webmaster for approval."


def test_add_product_to_cart(browser, base_url):
    """
    Dz10. Adds product in amount of 3 to cart and check if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    browser.get(base_url + '/opencart/index.php?route=product/product&product_id=40')
    quantity = browser.find_element(*ProductPageLocators.QUANTITY_INPUT)
    quantity.send_keys(Keys.BACKSPACE)
    quantity.send_keys(3)
    btn = browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
    btn.click()
    alert = browser.find_elements(*ProductPageLocators.ALERTS)[0]

    assert "Success" in alert.text
