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
    admin_login_page.login("admin", "admin")
    url_with_token = admin_login_page.get_current_url()
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
    admin_login_page.login("admin", "admin")
    url_with_token = admin_login_page.get_current_url()
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields("Tesla", "mytag", "Model Y")
    add_and_edit_page.click_save_button()
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    searched_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    admin_products_page.click_edit_button(searched_product)
    new_model = add_and_edit_page.edit_model("new model")
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    edited_product = admin_products_page.search_product_in_table(product_data[0], new_model)

    assert edited_product


@pytest.mark.dz11
def test_delete_product(browser, base_url):
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open()
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page.login("admin", "admin")
    url_with_token = admin_login_page.get_current_url()
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields("test", "test", "test")
    add_and_edit_page.click_save_button()
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    searched_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    admin_products_page\
        .check_product(searched_product)\
        .click_delete_button()
    Alert(browser).accept()
    deleted_product = admin_products_page.search_product_in_table(product_data[0], product_data[1])
    assert deleted_product is None
