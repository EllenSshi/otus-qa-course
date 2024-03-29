import allure
import time
from pages.AdminLoginPage import AdminLoginPage


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Valid authorization")
@allure.title("Authorization as admin")
def test_admin_login(remote_browser, base_url, logger_fixture):
    logger_fixture.info("===== test_admin_login =====")
    admin_login_page = AdminLoginPage(remote_browser, base_url)
    admin_login_page.open(logger_fixture)
    admin_login_page.login("user", "bitnami1")
    time.sleep(5)
    admin_login_page.check_if_admin_logged_in()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Authorization")
@allure.story("Invalid authorization")
@allure.title("Authorization as nonexistent user")
def test_nonexistent_login(remote_browser, base_url, logger_fixture):
    logger_fixture.info("===== test_admin_login =====")
    admin_login_page = AdminLoginPage(remote_browser, base_url)
    admin_login_page\
        .open(logger_fixture)\
        .login("admin", "a123")\
        .check_invalid_auth_msg()
