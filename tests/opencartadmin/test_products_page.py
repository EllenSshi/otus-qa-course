from pages.locators import AdminAddProductPage
from pages.locators import AdminLoginPageLocators
from pages.locators import AdminProductsPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


def authorization(browser):
    username = browser.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
    username.send_keys("admin")
    password = browser.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
    password.send_keys("admin")
    password.send_keys(Keys.ENTER)


def fill_in_necessary_product_fields(browser, name="Tesla", model="Model Y"):
    product_data = []
    product_name = browser.find_element(*AdminAddProductPage.PRODUCT_NAME_INPUT)
    product_name.send_keys(name)
    product_data.append(product_name.get_attribute("value"))
    meta_tag_title = browser.find_element(*AdminAddProductPage.META_TAG_TITLE_INPUT)
    meta_tag_title.send_keys("mytesla")
    browser.find_element(*AdminAddProductPage.DATA_TAB).click()
    product_model = browser.find_element(*AdminAddProductPage.MODEL_INPUT)
    product_model.send_keys(model)
    product_data.append(product_model.get_attribute("value"))
    return product_data


def search_product_in_table(browser, name, model):
    products = browser.find_elements(*AdminProductsPage.RANDOM_PRODUCT)
    for pr in products:
        tds = pr.get_property("childNodes")
        if tds[5].text == name and tds[7].text == model:
            return pr
    return None


def test_add_new_product(browser, base_url):
    browser.get(
        base_url + '/opencart/admin/index.php?route=catalog/product&user_token=w2lFNch22HwgP9i00euVDJteZjFt1HyB'
    )
    authorization(browser)
    browser.find_element(*AdminProductsPage.ADD_NEW_BUTTON).click()
    product_data = fill_in_necessary_product_fields(browser)
    price = browser.find_element(*AdminAddProductPage.PRICE_INPUT)
    price.clear()
    price.send_keys("1000000")
    quantity = browser.find_element(*AdminAddProductPage.QUANTITY_INPUT)
    quantity.clear()
    quantity.send_keys("5")
    browser.find_element(*AdminAddProductPage.SAVE_BTN).click()

    searched_product = search_product_in_table(browser, product_data[0], product_data[1])

    assert searched_product


def test_edit_product(browser, base_url):
    browser.get(
        base_url + '/opencart/admin/index.php?route=catalog/product&user_token=w2lFNch22HwgP9i00euVDJteZjFt1HyB')
    authorization(browser)
    products = browser.find_elements(*AdminProductsPage.RANDOM_PRODUCT)
    print(products.get_property("childNodes")[5].text)


def test_delete_product(browser, base_url):
    browser.get(
        base_url + '/opencart/admin/index.php?route=catalog/product&user_token=w2lFNch22HwgP9i00euVDJteZjFt1HyB'
    )
    authorization(browser)
    # firstly we need to add product we ae going to delete
    browser.find_element(*AdminProductsPage.ADD_NEW_BUTTON).click()
    product_data = fill_in_necessary_product_fields(browser, name="test", model="test")
    browser.find_element(*AdminAddProductPage.SAVE_BTN).click()
    # secondly we need to find added product
    searched_product = search_product_in_table(browser, product_data[0], product_data[1])
    # thirdly we click on checkbox of added product and click on delete button
    checkbox = searched_product.get_property("childNodes")[1].get_property("childNodes")[1]
    checkbox.click()
    browser.find_element(*AdminProductsPage.DELETE_BUTTON).click()
    # we are sure we want to delete it and accept alert
    Alert(browser).accept()
    # check whether our product was deleted
    assert search_product_in_table(browser, product_data[0], product_data[1]) is None
