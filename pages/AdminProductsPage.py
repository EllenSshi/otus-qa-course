import allure
import logging
from pages.BasePage import BasePage
from pages.locators import AdminProductsPageLocators

logger = logging.getLogger(__name__)


class AdminProductsPage(BasePage, AdminProductsPageLocators):
    path = '/opencart/admin/index.php?route=catalog/product'

    @allure.step("Click 'add new' button")
    def click_add_new_button(self):
        self._click(self.ADD_NEW_BUTTON)

    @allure.step("Click 'edit' button")
    def click_edit_button(self, element):
        edit_button = element.get_property("childNodes")[15].get_property("childNodes")[0]
        edit_button.wrapped_element.click()

    @allure.step("Click 'delete' button")
    def click_delete_button(self):
        self._click(self.DELETE_BUTTON)
        return self

    @allure.step("Click product checkbox")
    def check_product(self, element):
        checkbox = element.get_property("childNodes")[1].get_property("childNodes")[1]
        checkbox.click()
        return self

    @allure.step("Search and return product in table")
    def search_product_in_table(self, name, model):
        products = self.driver.find_elements(*self.RANDOM_PRODUCT)
        for product in products:
            tds = product.get_property("childNodes")
            if tds[5].text == name and tds[7].text == model:
                return product
        return None
