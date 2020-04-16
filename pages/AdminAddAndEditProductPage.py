import logging
import os
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.locators import AdminAddAndEditProductPageLocators

logger = logging.getLogger(__name__)


class AdminAddAndEditProductPage(BasePage, AdminAddAndEditProductPageLocators):
    path = ''

    def fill_in_necessary_product_fields(self, name, tag, model):
        product_data = []
        self._input(self.PRODUCT_NAME_INPUT, name)
        product_data.append(self._get_element_text(self.PRODUCT_NAME_INPUT))
        self._input(self.META_TAG_TITLE_INPUT, tag)
        self._click(self.DATA_TAB)
        self._input(self.MODEL_INPUT, model)
        product_data.append(self._get_element_text(self.MODEL_INPUT))
        return product_data

    def click_save_button(self):
        self._click(self.SAVE_BTN)

    def edit_model(self, value):
        self._click(self.DATA_TAB)
        self._wait_for_visibility(self.MODEL_INPUT)
        self._input(self.MODEL_INPUT, value)
        new_model = self._get_element_text(self.MODEL_INPUT)
        self.click_save_button()
        return new_model

    def upload_image(self, file):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file)
        self._click(self.IMAGE_TAB)
        self._click(self.IMAGE)
        self._click(self.EDIT_IMAGE_BTN)
        self._wait_for_visibility(self.UPLOAD_BTN)
        self.driver.execute_script("$('#button-upload').click();")
        self.driver.find_elements_by_css_selector('input[type=file]')[0].send_keys(filename)
        self.accept_alert()
        locator = f'a[href$="{file}"]'
        self._wait_for_visibility((By.CSS_SELECTOR, locator))
        self._click((By.CSS_SELECTOR, locator))
