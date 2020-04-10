from .BasePage import BasePage
from pages.locators import SearchResultsPageLocators


class SearchResultsPage(BasePage, SearchResultsPageLocators):
    path = '/opencart/index.php?route=product/search&search=iphone'

    def find_elements(self):
        self._wait_for_visibility(self.PRODUCT_SEARCH_BLOCK)
        self._wait_for_visibility(self.SEARCH_RESULTS)
        self._wait_for_visibility(self.SEARCH_INPUT)
        self._wait_for_visibility(self.CATEGORY_SELECT)
        self._wait_for_visibility(self.SUB_CATEGORY_CHECKBOX)
        self._wait_for_visibility(self.SEARCH_IN_DESCRIPTION_CHECKBOX)
        self._wait_for_visibility(self.SEARCH_BTN)
