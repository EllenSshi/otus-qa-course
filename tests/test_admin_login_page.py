from pages.AdminLoginPage import AdminLoginPage


def test_admin_login_page(browser, base_url):
    """
    Dz9. Just finding of elements on the admin login page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create admin_login_page object
    admin_login_page = AdminLoginPage(browser, base_url)
    # open page
    admin_login_page.open()
    # find some elements on this page
    admin_login_page.find_elements()
