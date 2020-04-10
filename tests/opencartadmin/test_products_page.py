import pytest
from selenium.webdriver.common.alert import Alert
from pages.AdminProductsPage import AdminProductsPage
from pages.AdminLoginPage import AdminLoginPage
from pages.AdminAddAndEditProductPage import AdminAddAndEditProductPage


@pytest.mark.dz11
def test_add_new_product(browser, base_url):
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open()
    admin_login_page = AdminLoginPage(browser, base_url)
    url_with_token = admin_login_page.login("admin", "admin")
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields("Tesla", "mytag", "Model Y")
    add_and_edit_page.click_save_button()
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    searched_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])

    assert searched_product


@pytest.mark.dz11
def test_edit_product(browser, base_url):
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open()
    admin_login_page = AdminLoginPage(browser, base_url)
    url_with_token = admin_login_page.login("admin", "admin")
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields("Tesla", "mytag", "Model Y")
    add_and_edit_page.click_save_button()
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    searched_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    # click on edit button of added product and edit product data
    admin_products_page.click_edit_button(searched_product)
    # edit model and click on save button
    new_model = add_and_edit_page.edit_model("new model")
    # then we want to check whether model of our product was changed
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    edited_product = admin_products_page.search_product_in_table(product_data[0], new_model)

    assert edited_product


@pytest.mark.dz11
def test_delete_product(browser, base_url):
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open()
    admin_login_page = AdminLoginPage(browser, base_url)
    url_with_token = admin_login_page.login("admin", "admin")
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    # firstly we need to add product we ae going to delete
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields("test", "test", "test")
    add_and_edit_page.click_save_button()
    # secondly we need to find added product
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    searched_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    # thirdly we click on checkbox of added product and click on delete button
    admin_products_page\
        .check_product(searched_product)\
        .click_delete_button()
    # we are sure we want to delete it and accept alert
    Alert(browser).accept()
    # check whether our product was deleted
    deleted_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    assert deleted_product is None
