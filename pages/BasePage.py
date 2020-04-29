import allure
from abc import abstractmethod
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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

    def open(self, logger):
        with allure.step(f"Go to {self.url}"):
            self.driver.get(self.url)
            logger.info(f"Произошел переход на страницу {str(self)} {self.url}")
            return self

    def __element(self, selector: tuple, index: int = None):
        if index:
            return self.driver.find_elements(*selector)[index]
        else:
            return self.driver.find_element(*selector)

    def _wait_for_visibility(self, selector, index=None, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))

    def _input(self, selector, value, index=None):
        with allure.step(f"Input into {selector} value '{value}'"):
            element = self.__element(selector, index)
            element.clear()
            element.send_keys(value)

    def _get_element_text(self, selector, index=None):
        element = self.__element(selector, index)
        return element.get_attribute("value")

    def _press_key(self, selector, key, index=None):
        element = self.__element(selector, index)
        element.send_keys(key)

    def _click(self, selector, index=None):
        with allure.step(f"Click on {selector}"):
            ActionChains(self.driver).move_to_element(self.__element(selector, index).wrapped_element).click().perform()
            # self.__element(selector, index).wrapped_element.click()

    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Check if admin logged in admin part")
    def check_if_admin_logged_in(self):
        try:
            self._wait_for_visibility(self.USER_ICON)
        except NoSuchElementException as e:
            raise AssertionError(e.msg)

    def accept_alert(self, wait=5):
        WebDriverWait(self.driver, wait).until(EC.alert_is_present())
        Alert(self.driver).accept()
