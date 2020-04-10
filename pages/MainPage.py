from .BasePage import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    path = '/opencart/'

    def find_elements(self):
        self._wait_for_visibility(self.SLIDESHOW)
        self._wait_for_visibility(self.SLIDESHOW_PAGINATION)
        self._wait_for_visibility(self.FEATURED_BLOCK)
        self._wait_for_visibility(self.CAROUSEL)
        self._wait_for_visibility(self.CAROUSEL_PAGINATION)
