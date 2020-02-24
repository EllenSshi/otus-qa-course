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


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = ChromeOptions()
        options.headless = True
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.headless = True
        browser = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        browser = webdriver.Safari()
    else:
        raise pytest.UsageError("Undefined --browser_name. Should be 'chrome', 'firefox' or 'safari'")

    # browser.fullscreen_window()  # не работает с chrome
    yield browser
    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")