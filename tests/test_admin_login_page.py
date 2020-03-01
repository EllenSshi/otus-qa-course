from pages.locators import AdminLoginPageLocators


def test_admin_login_page(browser, base_url):
    browser.get(base_url + '/opencart/admin/')
    browser.find_element(*AdminLoginPageLocators.USERNAME_INPUT)
    browser.find_element(*AdminLoginPageLocators.PASSWORD_INPUT)
    browser.find_element(*AdminLoginPageLocators.FORGOTTEN_PASSWORD_LINK)
    browser.find_element(*AdminLoginPageLocators.LOGIN_BTN)
    browser.find_element(*AdminLoginPageLocators.FOOTER)
