import allure
import datetime
import logging
import mysql.connector
import sys
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from sshtunnel import SSHTunnelForwarder

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
        default="selenoid"
    )

@pytest.fixture
def db_cursor():
    server = SSHTunnelForwarder(
        '192.168.56.101',
        ssh_username='user',
        ssh_password='admin',
        remote_bind_address=('127.0.0.1', 3306)
    )
    server.start()

    config = {
        "user": "user",
        "password": "123",
        "host": "127.0.0.1",
        "port": server.local_bind_port,
        "database": "opencart"
    }
    time.sleep(3)
    connection = mysql.connector.connect(**config)
    connection.autocommit = True
    db_cursor = connection.cursor()
    yield db_cursor
    db_cursor.close()
    connection.close()
    server.stop()
    if db_cursor and connection:
        db_cursor.close()
        connection.close()


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
        options.headless = False
    elif browser == "firefox":
        options = FirefoxOptions()
        options.headless = False
    executor = request.config.getoption("--executor")
    wd = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                          desired_capabilities={
                              "browserName": browser,
                              "version": "81.0",
                              "enableVnc": True,
                              "enableVideo": False
                          },
                          options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture
def browserstack_browser():
    BROWSERSTACK_URL = 'https://alyonashishkina1:socxM3cpEhSDs4YpMBbe@hub-cloud.browserstack.com/wd/hub'
    desired_cap = {

        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': '80',
        'name': "alyonashishkina1's First Test"

    }
    driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)
    yield driver
    driver.quit()


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
        scr_name = driver.name + ' ' + str(now)
        scr_body = driver.get_screenshot_as_png()
        # driver.save_screenshot(f'tests/screenshots/{scr_name}.png')
        allure.attach(name=scr_name, body=scr_body, attachment_type=allure.attachment_type.PNG)
