from .BasePage import BasePage
from pages.locators import AdminLoginPageLocators


class AdminLoginPage(BasePage, AdminLoginPageLocators):
    path = '/opencart/admin/'

    def find_elements(self):
        self._wait_for_visibility(self.USERNAME_INPUT)
        self._wait_for_visibility(self.PASSWORD_INPUT)
        self._wait_for_visibility(self.FORGOTTEN_PASSWORD_LINK)
        self._wait_for_visibility(self.LOGIN_BTN)
        self._wait_for_visibility(self.FOOTER)
