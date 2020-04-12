from .BasePage import BasePage
from pages.locators import CatalogPageLocators


class CatalogPage(BasePage, CatalogPageLocators):
    path = '/opencart/index.php?route=product/category&path=20'

    def find_elements(self):
        self._wait_for_visibility(self.LIST_GROUP)
        self._wait_for_visibility(self.LIST_BTN)
        self._wait_for_visibility(self.GRID_BTN)
        self._wait_for_visibility(self.COMPARE_LINK)
        self._wait_for_visibility(self.SORT_INPUT)
        self._wait_for_visibility(self.SHOW_INPUT)
