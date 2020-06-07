import allure
import random

from pages.ComparisonPage import ComparisonPage
from pages.ProductPage import ProductPage


@allure.feature("Product comparison")
@allure.story("Add one product to comparison page")
@allure.title("Add product to product comparison")
def test_add_to_product_comparison(remote_browser, base_url, logger_fixture):
    logger_fixture.info("===== test_add_to_product_comparison =====")
    product_page = ProductPage(remote_browser, base_url)
    product_page.open(logger_fixture)
    product_name = product_page.get_product_name()
    product_page\
        .click_compare_button()\
        .click_comparison_link()
    comparison_page = ComparisonPage(remote_browser, base_url)

    with allure.step("Check if product name and name form comparison page are the same"):
        assert product_name == comparison_page.get_first_product_name()


@allure.feature("Product review")
@allure.story("Send review with valid data")
@allure.title("Send review")
def test_send_review(remote_browser, base_url, logger_fixture):
    """
    dz10. Sends review about product and checks if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_send_review =====")
    product_page = ProductPage(remote_browser, base_url)
    product_page\
        .open(logger_fixture)\
        .click_review_tab()\
        .fill_review_fields("Name", "This is my first review ever")
    rating = random.randint(0, 4)
    product_page\
        .click_rating(rating)\
        .click_review_button()
    alert = product_page.get_success_alert()
    expected_text = "Thank you for your review. It has been submitted to the webmaster for approval."
    with allure.step(f"Check if text '{expected_text}' is present in alert"):
        assert alert.text == expected_text


@allure.feature("Add product to cart")
@allure.story("Valid product")
@allure.title("Add product to cart")
def test_add_product_to_cart(remote_browser, base_url, logger_fixture):
    """
    Dz10. Adds product in random amount to cart and check if successful alert would appear
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_add_product_to_cart =====")
    product_page = ProductPage(remote_browser, base_url)
    product_page\
        .open(logger_fixture)\
        .fill_product_quantity(random.randint(1, 5))\
        .click_add_to_cart()
    alert = product_page.get_success_alert()
    expected_text = "Success"
    with allure.step(f"Check if text '{expected_text}' is present in alert"):
        assert expected_text in alert.text
