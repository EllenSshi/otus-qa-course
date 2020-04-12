import pytest
from selenium.webdriver.common.alert import Alert
from pages.AdminProductsPage import AdminProductsPage
from pages.AdminLoginPage import AdminLoginPage
from pages.AdminAddAndEditProductPage import AdminAddAndEditProductPage


def login_and_add_new_product(browser, base_url, username, userpassword, pname, ptag, pmodel):
    data = {}
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open()
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page.login(username, userpassword)
    data['url_with_token'] = admin_login_page.get_current_url()
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields(pname, ptag, pmodel)
    data['pname'] = product_data[0]
    data['pmodel'] = product_data[1]
    add_and_edit_page.click_save_button()
    return data


@pytest.mark.dz11
def test_add_new_product(browser, base_url):
    data = login_and_add_new_product(browser, base_url, "admin", "admin", "Tesla", "mytag", "Model Y")
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    admin_products_page = AdminProductsPage(browser, base_url)
    searched_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    assert searched_product


@pytest.mark.dz11
def test_edit_product(browser, base_url):
    data = login_and_add_new_product(browser, base_url, "admin", "admin", "Tesla", "mytag", "Model Y")
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    admin_products_page = AdminProductsPage(browser, base_url)
    searched_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    admin_products_page.click_edit_button(searched_product)
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    new_model = add_and_edit_page.edit_model("new model")
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    edited_product = admin_products_page.search_product_in_table(data['pname'], new_model)
    assert edited_product


@pytest.mark.dz11
def test_delete_product(browser, base_url):
    data = login_and_add_new_product(browser, base_url, "admin", "admin", "test", "test", "test")
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    admin_products_page = AdminProductsPage(browser, base_url)
    searched_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    admin_products_page\
        .check_product(searched_product)\
        .click_delete_button()
    Alert(browser).accept()
    deleted_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    assert deleted_product is None
