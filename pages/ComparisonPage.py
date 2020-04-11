from pages.BasePage import BasePage
from pages.locators import ComparisonPageLocators


class ComparisonPage(BasePage, ComparisonPageLocators):
    path = '/opencart/index.php?route=product/compare'

    def get_first_product_name(self):
        return self._get_element_text(self.PRODUCT_NAME)
