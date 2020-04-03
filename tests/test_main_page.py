from pages.locators import MainPageLocators


def test_main_page(browser, base_url):
    """
    Dz9. Just finding of elements on the main page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    browser.get(base_url + '/opencart/index.php?route=common/home')
    browser.find_element(*MainPageLocators.SLIDESHOW)
    browser.find_element(*MainPageLocators.SLIDESHOW_PAGINATION)
    browser.find_element(*MainPageLocators.FEATURED_BLOCK)
    browser.find_element(*MainPageLocators.CAROUSEL)
    browser.find_element(*MainPageLocators.CAROUSEL_PAGINATION)
