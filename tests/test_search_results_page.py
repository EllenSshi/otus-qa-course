from pages.locators import SearchResultsPageLocators


def test_search_results_page(browser, base_url):
    """
    Dz9. Just finding of elements on the search results page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    browser.get(base_url + '/opencart/index.php?route=product/search&search=iphone')
    browser.find_element(*SearchResultsPageLocators.PRODUCT_SEARCH_BLOCK)
    browser.find_element(*SearchResultsPageLocators.SEARCH_RESULTS)
    browser.find_element(*SearchResultsPageLocators.SEARCH_INPUT)
    browser.find_element(*SearchResultsPageLocators.CATEGORY_SELECT)
    browser.find_element(*SearchResultsPageLocators.SUB_CATEGORY_CHECKBOX)
    browser.find_element(*SearchResultsPageLocators.SEARCH_IN_DESCRIPTION_CHECKBOX)
    browser.find_element(*SearchResultsPageLocators.SEARCH_BTN)
