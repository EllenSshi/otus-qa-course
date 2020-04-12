from .BasePage import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage, MainPageLocators):
    path = '/opencart/'

    def check_featured_block_is_not_empty(self):
        self._wait_for_visibility(self.FEATURED_BLOCK_IMAGES, 0)
        self._wait_for_visibility(self.FEATURED_BLOCK_CAPTIONS, 0)
        self._wait_for_visibility(self.FEATURED_BLOCK_BTN_GROUPS, 0)
