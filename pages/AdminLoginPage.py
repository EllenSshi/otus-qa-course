import allure
import logging

from selenium.common.exceptions import NoSuchElementException

from .BasePage import BasePage
from pages.locators import AdminLoginPageLocators
from pages.locators import BasePageLocators

logger = logging.getLogger(__name__)


class AdminLoginPage(BasePage, AdminLoginPageLocators, BasePageLocators):
    path = '/opencart/admin/'

    @allure.step("Sign in admin part")
    def login(self, username, password):
        """
        This function is for signing in admin part of site
        """
        self._input(self.USERNAME_INPUT, username)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BTN)
        return self

    @allure.step("Check if invalid auth message appeared")
    def check_invalid_auth_msg(self):
        try:
            self._wait_for_visibility(self.INVALID_AUTH_MSG)
        except NoSuchElementException as e:
            raise AssertionError(e.msg)
