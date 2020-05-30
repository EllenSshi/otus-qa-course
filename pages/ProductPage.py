import logging
from pages.BasePage import BasePage
from pages.locators import ProductPageLocators

logger = logging.getLogger(__name__)


class ProductPage(BasePage, ProductPageLocators):
    path = '/opencart/index.php?route=product/product&product_id=40'

    def fill_product_quantity(self, quantity: int):
        self._input(self.QUANTITY_INPUT, quantity)
        return self

    def click_add_to_cart(self):
        self._click(self.ADD_TO_CART_BTN)

    def click_review_tab(self):
        self._wait_for_visibility(self.REVIEW_TAB)
        self._click(self.REVIEW_TAB)
        return self

    def fill_review_fields(self, review_name, review_text):
        self._wait_for_visibility(self.REVIEW_NAME_INPUT)
        self._input(self.REVIEW_NAME_INPUT, review_name)
        self._wait_for_visibility(self.REVIEW_TEXT_INPUT)
        self._input(self.REVIEW_TEXT_INPUT, review_text)

    def click_rating(self, index):
        self._click(self.REVIEW_RATING_MARKS, index)
        return self

    def click_review_button(self):
        self._click(self.REVIEW_BTN)

    def get_success_alert(self):
        alert = self._wait_for_visibility(self.ALERTS, 0)
        return alert

    def click_compare_button(self):
        self._click(self.COMPARE_BTN)
        return self

    def click_comparison_link(self):
        self._click(self.COMPARISON_LINK)
        return self

    def get_product_name(self):
        return self._get_element_text(self.PRODUCT_NAME)
