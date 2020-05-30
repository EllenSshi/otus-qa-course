import time

import allure
import pytest
from pages.AdminProductsPage import AdminProductsPage
from pages.AdminLoginPage import AdminLoginPage
from pages.AdminAddAndEditProductPage import AdminAddAndEditProductPage


@allure.step("Log in and add new product")
def login_and_add_new_product(browser, base_url, username, userpassword, pname, ptag, pmodel, logger_fixture):
    data = {}
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open(logger_fixture)
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page.login(username, userpassword)
    data['url_with_token'] = admin_login_page.get_current_url()
    admin_products_page.click_add_new_button()
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    product_data = add_and_edit_page.fill_in_necessary_product_fields(pname, ptag, pmodel)
    data['pname'] = product_data[0]
    data['pmodel'] = product_data[1]

    return data


@allure.feature("Work with products list")
@allure.story("Add new product")
@allure.title("Add new product with valid data")
@pytest.mark.dz11
def test_add_new_product(browser, base_url, logger_fixture):
    logger_fixture.info("===== test_add_new_product =====")
    data = login_and_add_new_product(browser, base_url, "admin", "admin", "Tesla", "mytag", "Model Y", logger_fixture)
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    add_and_edit_page.upload_image("ModelY.jpg")
    add_and_edit_page.click_save_button()
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    admin_products_page = AdminProductsPage(browser, base_url)
    searched_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    assert searched_product


@allure.feature("Work with products list")
@allure.story("Edit product")
@allure.title("Edit product with valid data")
@pytest.mark.dz11
def test_edit_product(browser, base_url, logger_fixture, db_cursor):
    logger_fixture.info("===== test_edit_product =====")
    # data = login_and_add_new_product(browser, base_url, "admin", "admin", "Tesla", "mytag", "Model Y", logger_fixture)
    # add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    # add_and_edit_page.click_save_button()
    name = "fooname"
    model = "foomodel"
    add_new_product_through_db(db_cursor, name, model)
    admin_products_page = AdminProductsPage(browser, base_url)
    admin_products_page.open(logger_fixture)
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page.login("admin", "admin")
    url_with_token = admin_login_page.get_current_url()

    searched_product = admin_products_page.search_product_in_table(name, model)
    admin_products_page.click_edit_button(searched_product)
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    new_model = "new model"
    add_and_edit_page.edit_model(new_model)
    browser.get(url_with_token)  # HOW TO GET RID OF IT ???
    edited_product = admin_products_page.search_product_in_table(name, new_model)
    assert edited_product


@allure.feature("Work with products list")
@allure.story("Delete product")
@allure.title("Delete product from table")
@pytest.mark.dz11
def test_delete_product(browser, base_url, logger_fixture, db_cursor):
    logger_fixture.info("===== test_delete_product =====")
    data = login_and_add_new_product(browser, base_url, "admin", "admin", "test", "test", "test", logger_fixture)
    add_and_edit_page = AdminAddAndEditProductPage(browser, base_url)
    add_and_edit_page.click_save_button()
    browser.get(data['url_with_token'])  # HOW TO GET RID OF IT ???
    admin_products_page = AdminProductsPage(browser, base_url)
    searched_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    admin_products_page\
        .check_product(searched_product)\
        .click_delete_button()\
        .accept_alert()
    deleted_product = admin_products_page.search_product_in_table(data['pname'], data['pmodel'])
    assert deleted_product is None

    # проверка, что удаленного продукта нет в базе данных
    with open('select_product.sql', 'r') as script:
        db_cursor.execute(script.read(), (data['pname'], data['pmodel']))
    assert not db_cursor.fetchall()


def add_new_product_through_db(db_cursor, name, model):
    with open('insert_into_product.sql', 'r') as script:
        db_cursor.execute(script.read(), (model,))

    script = "Select * from oc_product where oc_product.model=%s"
    db_cursor.execute(script, (model,))
    product_id = db_cursor.fetchone()[0]

    with open('insert_into_product_description.sql', 'r') as script:
        db_cursor.execute(script.read(), (product_id, name))
