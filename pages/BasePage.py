from abc import abstractmethod

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage(BasePageLocators):
    def __init__(self, driver, base_url='http://192.168.56.101'):
        self.driver = driver
        self.base_url = base_url

    @property
    @abstractmethod
    def path(self):
        return self.path

    @property
    def url(self):
        return self.base_url + self.path

    def open(self):
        self.driver.get(self.url)
        return self

    def __element(self, selector: tuple, index: int = 0):
        return self.driver.find_elements(*selector)[index]

    def _wait_for_visibility(self, selector, index=0, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _get_element_text(self, selector, index=0):
        element = self.__element(selector, index)
        return element.get_attribute("value")

    def _press_key(self, selector, key, index=0):
        element = self.__element(selector, index)
        element.send_keys(key)

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def get_current_url(self):
        return self.driver.current_url

    def check_if_admin_logged_in(self):
        self._wait_for_visibility(self.USER_ICON)
