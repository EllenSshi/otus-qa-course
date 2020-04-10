from .BasePage import BasePage
from pages.locators import AdminLoginPageLocators
from selenium.webdriver.common.keys import Keys


class AdminLoginPage(BasePage, AdminLoginPageLocators):
    path = '/opencart/admin/'

    def find_elements(self):
        self._wait_for_visibility(self.USERNAME_INPUT)
        self._wait_for_visibility(self.PASSWORD_INPUT)
        self._wait_for_visibility(self.FORGOTTEN_PASSWORD_LINK)
        self._wait_for_visibility(self.LOGIN_BTN)
        self._wait_for_visibility(self.FOOTER)

    def login(self, username, password):
        """
        This function is for signing in admin part of site
        """
        self._input(self.USERNAME_INPUT, username)
        self._input(self.PASSWORD_INPUT, password)
        self._press_key(self.PASSWORD_INPUT, Keys.ENTER)
        return self.driver.current_url
