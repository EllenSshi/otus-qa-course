import datetime
import logging
import sys

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

logger = logging.getLogger("driver")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)s %(message)s',
                              datefmt='%d.%m.%Y %H:%M:%S')
# fh = logging.FileHandler("my.log")
# fh.setLevel(logging.INFO)
# fh.setFormatter(formatter)
# logger.addHandler(fh)
#
# sh = logging.StreamHandler(sys.stdout)
# sh.setLevel(logging.INFO)
# sh.setFormatter(formatter)
# logger.addHandler(sh)


@pytest.fixture(autouse=True, scope="session")
def logger_fixture(request):
    logfile = request.config.getoption("--logfile")
    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    else:
        sh = logging.StreamHandler(sys.stdout)
        sh.setLevel(logging.INFO)
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger


# @pytest.fixture(autouse=True)
# def logger_fixture(request):
#     logfile = request.config.getoption("--logfile")
#     if logfile:
#         logging.basicConfig(filename=logfile,
#                             format='%(asctime)s %(name)s %(filename)s:%(lineno)s %(message)s',
#                             datefmt='%d.%m.%Y %H:%M:%S')
#
#         logger = logging.getLogger("driver")
#         logger.setLevel(logging.INFO)
#     else:
#         logging.basicConfig(format='%(asctime)s %(name)s %(filename)s:%(lineno)s %(message)s',
#                             datefmt='%d.%m.%Y %H:%M:%S')
#
#         logger = logging.getLogger("driver")
#         logger.setLevel(logging.INFO)
#     return logger


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "safari"],
        help="Which browser to use for running tests"
    )
    parser.addoption(
        "--base_url",
        default="http://192.168.56.101",
        help="Base url of your Opencart application"
    )
    parser.addoption(
        "--wait",
        default=3,
        type=int,
        help="Implicity wait for browser"
    )
    parser.addoption(
        "--logfile",
        default=None,
        help="File to save logs in"
    )
    parser.addoption(
        "--executor",
        default="192.168.56.1",
        help="File to save logs in"
    )


@pytest.fixture
def browser(request):
    logger.info("Browser start..")
    browser_name = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.headless = False
        # options.add_argument("--kiosk")  # эта штука для mac os, вместо start-maximized (не работало)
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'ALL'}
        browser = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=dc), MyListener())
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.headless = True
        options.add_argument("--kiosk")
        browser = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        browser = webdriver.Safari()
        browser.fullscreen_window()  # не нашла SafariOptions в библиотеке Selenium
    else:
        raise pytest.UsageError("Undefined --browser_name. Should be 'chrome', 'firefox' or 'safari'")

    browser.implicitly_wait(wait)
    yield browser
    browser_logs = browser.get_log("browser")
    if len(browser_logs) > 0:
        logger.warning("There are some errors in browser log!")
    browser.quit()


@pytest.fixture
def remote_browser(request):
    browser = request.config.getoption("--browser")
    options = None
    if browser == "chrome":
        options = ChromeOptions()
        options.headless = True
    elif browser == "firefox":
        options = FirefoxOptions()
        options.headless = True
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={"browserName": browser}, options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


class MyListener(AbstractEventListener):
    def after_change_value_of(self, element, driver):
        logger.info(f'Value of element {element.tag_name} was changed with <{element.get_attribute("value")}>')

    def before_click(self, element, driver):
        logger.info(f'Click on element {element.tag_name}')

    def after_click(self, element, driver):
        logger.info(f'Successful click on element {element.tag_name}')

    def before_find(self, by, value, driver):
        logger.info(f'Find element by: {by}, value: {value}')

    def after_find(self, by, value, driver):
        logger.info(f'Element was found by: {by}, value: {value}')

    def after_quit(self, driver):
        logger.info('Driver quit')

    def on_exception(self, exception, driver):
        logger.error(exception.msg)
        now = datetime.datetime.now()
        driver.save_screenshot(f'tests/screenshots/{driver.name} {now}.png')
