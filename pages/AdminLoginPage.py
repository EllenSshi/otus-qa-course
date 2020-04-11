from .BasePage import BasePage
from pages.locators import AdminLoginPageLocators
from pages.locators import BasePageLocators
from selenium.webdriver.common.keys import Keys


class AdminLoginPage(BasePage, AdminLoginPageLocators, BasePageLocators):
    path = '/opencart/admin/'

    def login(self, username, password):
        """
        This function is for signing in admin part of site
        """
        self._input(self.USERNAME_INPUT, username)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BTN)
        return self
