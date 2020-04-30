import allure
from pages.AdminLoginPage import AdminLoginPage


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Valid authorization")
@allure.title("Authorization as admin")
def test_admin_login(browser, base_url, logger_fixture):
    logger_fixture.info("===== test_admin_login =====")
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page\
        .open(logger_fixture)\
        .login("admin", "admin1")\
        .check_if_admin_logged_in()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Invalid authorization")
@allure.title("Authorization as nonexistent user")
def test_nonexistent_login(browser, base_url, logger_fixture):
    logger_fixture.info("===== test_admin_login =====")
    admin_login_page = AdminLoginPage(browser, base_url)
    admin_login_page\
        .open(logger_fixture)\
        .login("admin", "a123")\
        .check_invalid_auth_msg()
