from pages.AdminLoginPage import AdminLoginPage


def test_admin_login(browser, base_url, logger_fixture):
    """
    Dz9. Just finding of elements on the admin login page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_admin_login =====")
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page\
        .open(logger_fixture)\
        .login("admin", "admin")\
        .check_if_admin_logged_in()
