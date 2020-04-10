import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators
from pages.ProductPage import ProductPage


def test_product_page(browser, base_url):
    """
    Dz9. Just finding of elements on the product page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create product_page object
    product_page = ProductPage(browser, base_url)
    # open page
    product_page.open()
    # find some elements on this page
    product_page.find_elements()


def test_send_review(browser, base_url):
    """
    dz10. Sends review about product and checks if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create product_page object
    product_page = ProductPage(browser, base_url)
    # open page
    product_page.open()
    # click review tab
    product_page.click_review_tab()
    # fill review name and review text
    product_page.fill_review_fields("Name", "This is my first review ever")
    # click random review rating
    rating = random.randint(0, 4)
    product_page.click_rating(rating)
    # click review button
    product_page.click_review_button()
    # check if alert text was success
    alert = product_page.get_success_alert()

    assert alert.text == "Thank you for your review. " \
                         "It has been submitted to the webmaster for approval."


def test_add_product_to_cart(browser, base_url):
    """
    Dz10. Adds product in amount of 3 to cart and check if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create product_page object
    product_page = ProductPage(browser, base_url)
    # open page
    product_page.open()
    # fill quantity of product
    product_page.fill_product_quantity(random.randint(1, 5))
    # click on add_to_cart button
    product_page.click_add_to_cart()
    # check if alert text was success
    alert = product_page.get_success_alert()

    assert "Success" in alert.text
