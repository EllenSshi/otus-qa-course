import random

from pages.ComparisonPage import ComparisonPage
from pages.ProductPage import ProductPage


def test_add_to_product_comparison(browser, base_url):
    product_page = ProductPage(browser, base_url)
    product_page.open()
    product_name = product_page.get_product_name()
    product_page\
        .click_compare_button()\
        .click_comparison_link()
    comparison_page = ComparisonPage(browser, base_url)

    assert product_name == comparison_page.get_first_product_name()


def test_send_review(browser, base_url):
    """
    dz10. Sends review about product and checks if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    product_page = ProductPage(browser, base_url)
    product_page\
        .open()\
        .click_review_tab()\
        .fill_review_fields("Name", "This is my first review ever")
    rating = random.randint(0, 4)
    product_page\
        .click_rating(rating)\
        .click_review_button()
    alert = product_page.get_success_alert()

    assert alert.text == "Thank you for your review. " \
                         "It has been submitted to the webmaster for approval."


def test_add_product_to_cart(browser, base_url):
    """
    Dz10. Adds product in random amount to cart and check if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    product_page = ProductPage(browser, base_url)
    product_page\
        .open()\
        .fill_product_quantity(random.randint(1, 5))\
        .click_add_to_cart()
    alert = product_page.get_success_alert()

    assert "Success" in alert.text
