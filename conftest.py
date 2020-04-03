import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions


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


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    wait = request.config.getoption("--wait")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.headless = True
        options.add_argument("--kiosk")  # эта штука для mac os, вместо start-maximized (не работало)
        browser = webdriver.Chrome(options=options)
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
    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")
