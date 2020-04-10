from pages.BasePage import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    path = '/opencart/index.php?route=product/product&product_id=40'

    def find_elements(self):
        self._wait_for_visibility(self.THUMBNAILS)
        self._wait_for_visibility(self.DESC_AND_REVIEW_TABS)
        self._wait_for_visibility(self.TAB_CONTENT)
        self._wait_for_visibility(self.QUANTITY_INPUT)
        self._wait_for_visibility(self.ADD_TO_CART_BTN)
        self._wait_for_visibility(self.RATING)

    def fill_product_quantity(self, quantity: int):
        self._input(self.QUANTITY_INPUT, quantity)

    def click_add_to_cart(self):
        self._click(self.ADD_TO_CART_BTN)

    def click_review_tab(self):
        self._wait_for_visibility(self.REVIEW_TAB)
        self._click(self.REVIEW_TAB)

    def fill_review_fields(self, review_name, review_text):
        self._wait_for_visibility(self.REVIEW_NAME_INPUT)
        self._input(self.REVIEW_NAME_INPUT, review_name)
        self._wait_for_visibility(self.REVIEW_TEXT_INPUT)
        self._input(self.REVIEW_TEXT_INPUT, review_text)

    def click_rating(self, index):
        self._click(self.REVIEW_RATING_MARKS, index)

    def click_review_button(self):
        self._click(self.REVIEW_BTN)

    def get_success_alert(self):
        alert = self._wait_for_visibility(self.ALERTS, 0)
        return alert
