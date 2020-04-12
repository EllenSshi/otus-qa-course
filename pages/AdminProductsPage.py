from pages.BasePage import BasePage
from pages.locators import AdminProductsPageLocators


class AdminProductsPage(BasePage, AdminProductsPageLocators):
    path = '/opencart/admin/index.php?route=catalog/product'

    def click_add_new_button(self):
        self._click(self.ADD_NEW_BUTTON)

    def click_edit_button(self, element):
        edit_button = element.get_property("childNodes")[15].get_property("childNodes")[0]
        edit_button.click()

    def click_delete_button(self):
        self._click(self.DELETE_BUTTON)

    def check_product(self, element):
        checkbox = element.get_property("childNodes")[1].get_property("childNodes")[1]
        checkbox.click()
        return self

    def search_product_in_table(self, name, model):
        products = self.driver.find_elements(*self.RANDOM_PRODUCT)
        for product in products:
            tds = product.get_property("childNodes")
            if tds[5].text == name and tds[7].text == model:
                return product
        return None
