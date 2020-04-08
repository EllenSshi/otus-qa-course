import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import AdminAddAndEditProductPage
from pages.locators import AdminLoginPageLocators
from pages.locators import AdminProductsPage


def authorization(browser, base_url):
    """
    This function is for signing in admin part of site
    """
    browser.get(
        base_url + '/opencart/admin/index.php?route=catalog/product'
    )
    username = browser.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
    username.send_keys("admin")
    password = browser.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
    password.send_keys("admin")
    password.send_keys(Keys.ENTER)
    return browser.current_url


def fill_in_necessary_product_fields(browser, name="Tesla", model="Model Y"):
    """
    This function is for filling in all necessary fields of product
    :param name: product name that will be used to create new product
    :param model: product model that will be used to create new product
    :return: list of two necessary fields of product - name and model
    """
    product_data = []
    browser.find_element(*AdminProductsPage.ADD_NEW_BUTTON).click()
    product_name = browser.find_element(*AdminAddAndEditProductPage.PRODUCT_NAME_INPUT)
    product_name.send_keys(name)
    product_data.append(product_name.get_attribute("value"))
    meta_tag_title = browser.find_element(*AdminAddAndEditProductPage.META_TAG_TITLE_INPUT)
    meta_tag_title.send_keys("mytesla")
    browser.find_element(*AdminAddAndEditProductPage.DATA_TAB).click()
    product_model = browser.find_element(*AdminAddAndEditProductPage.MODEL_INPUT)
    product_model.send_keys(model)
    product_data.append(product_model.get_attribute("value"))
    return product_data


def search_product_in_table(browser, name, model):
    """
    This function is for searching product in table by its name and model
    :return: WebElement with tag name = 'td' that contains product info
    or None if product was not found in table
    """
    products = browser.find_elements(*AdminProductsPage.RANDOM_PRODUCT)
    for product in products:
        tds = product.get_property("childNodes")
        if tds[5].text == name and tds[7].text == model:
            return product
    return None


@pytest.mark.dz11
def test_add_new_product(browser, base_url):
    catalog_products_link = authorization(browser, base_url)
    # firstly we need to fill in all necessary fields about product
    product_data = fill_in_necessary_product_fields(browser)
    # then we want to fill in some unnecessary fields about product
    price = browser.find_element(*AdminAddAndEditProductPage.PRICE_INPUT)
    price.clear()
    price.send_keys("1000000")
    quantity = browser.find_element(*AdminAddAndEditProductPage.QUANTITY_INPUT)
    quantity.clear()
    quantity.send_keys("5")
    # save all info about product
    browser.find_element(*AdminAddAndEditProductPage.SAVE_BTN).click()
    # make sure that created product presents in list of products
    browser.get(catalog_products_link)
    searched_product = search_product_in_table(browser, product_data[0], product_data[1])

    assert searched_product


@pytest.mark.dz11
def test_edit_product(browser, base_url):
    catalog_products_link = authorization(browser, base_url)
    # firstly we need to add product we ae going to edit
    product_data = fill_in_necessary_product_fields(browser, name="some name", model="old model")
    browser.find_element(*AdminAddAndEditProductPage.SAVE_BTN).click()
    # secondly we need to find added product
    browser.get(catalog_products_link)
    searched_product = search_product_in_table(browser, product_data[0], product_data[1])
    # thirdly we click on edit button of added product and edit product data
    edit_button = searched_product.get_property("childNodes")[15].get_property("childNodes")[0]
    edit_button.click()
    # then we want to edit model and click on save button
    browser.find_element(*AdminAddAndEditProductPage.DATA_TAB).click()
    explicit_wait = WebDriverWait(browser, 5)
    product_model = explicit_wait.until(
        EC.visibility_of_element_located(AdminAddAndEditProductPage.MODEL_INPUT)
    )
    product_model.clear()
    product_model.send_keys("new model")
    new_model = product_model.get_attribute("value")
    browser.find_element(*AdminAddAndEditProductPage.SAVE_BTN).click()
    # then we want to check whether model of our product was changed
    browser.get(catalog_products_link)
    edited_product = search_product_in_table(browser, product_data[0], new_model)

    assert edited_product


@pytest.mark.dz11
def test_delete_product(browser, base_url):
    catalog_products_link = authorization(browser, base_url)
    # firstly we need to add product we ae going to delete
    product_data = fill_in_necessary_product_fields(browser, name="test", model="test")
    browser.find_element(*AdminAddAndEditProductPage.SAVE_BTN).click()
    # secondly we need to find added product
    browser.get(catalog_products_link)
    searched_product = search_product_in_table(browser, product_data[0], product_data[1])
    # thirdly we click on checkbox of added product and click on delete button
    checkbox = searched_product.get_property("childNodes")[1].get_property("childNodes")[1]
    checkbox.click()
    browser.find_element(*AdminProductsPage.DELETE_BUTTON).click()
    # we are sure we want to delete it and accept alert
    Alert(browser).accept()
    # check whether our product was deleted
    assert search_product_in_table(browser, product_data[0], product_data[1]) is None
