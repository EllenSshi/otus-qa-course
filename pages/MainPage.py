import allure
import logging
from .BasePage import BasePage
from pages.locators import MainPageLocators

logger = logging.getLogger(__name__)


class MainPage(BasePage, MainPageLocators):
    path = '/opencart/'

    @allure.step("Check if featured block of main page is not empy")
    def check_featured_block_is_not_empty(self):
        self._wait_for_visibility(self.FEATURED_BLOCK_IMAGES, 0)
        self._wait_for_visibility(self.FEATURED_BLOCK_CAPTIONS, 0)
        self._wait_for_visibility(self.FEATURED_BLOCK_BTN_GROUPS, 0)
