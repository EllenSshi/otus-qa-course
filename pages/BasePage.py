from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url='http://192.168.56.101'):
        self.driver = driver
        self.base_url = base_url
        self.__path = ''

    @property
    def path(self):
        return self.__path

    @property
    def url(self):
        return self.base_url + self.path

    def open(self):
        self.driver.get(self.url)

    def __element(self, selector: tuple, index: int = 0):
        return self.driver.find_elements(*selector)[index]

    def _wait_for_visibility(self, selector, wait=3):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))
