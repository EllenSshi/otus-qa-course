from pages.locators import CatalogPageLocators


def test_catalog_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=product/category&path=20')
    browser.find_element(*CatalogPageLocators.LIST_GROUP)
    browser.find_element(*CatalogPageLocators.LIST_BTN)
    browser.find_element(*CatalogPageLocators.GRID_BTN)
    browser.find_element(*CatalogPageLocators.COMPARE_LINK)
    browser.find_element(*CatalogPageLocators.SORT_INPUT)
    browser.find_element(*CatalogPageLocators.SHOW_INPUT)
