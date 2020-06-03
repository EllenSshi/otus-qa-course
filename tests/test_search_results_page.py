import allure
from pages.SearchResultsPage import SearchResultsPage


@allure.feature("Search")
@allure.story("Search product by name")
@allure.title("Product results are displayed as list")
def test_products_displayed_as_list(remote_browser, base_url, logger_fixture):
    """
    Dz9. Just finding of elements on the search results page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    search_results_page = SearchResultsPage(remote_browser, base_url)
    logger_fixture.info("===== test_products_displayed_as_list =====")
    search_results_page\
        .open(logger_fixture)\
        .click_display_as_list()\
        .check_products_displayed_as_list()


@allure.feature("Search")
@allure.story("Search product by name")
@allure.title("Product results are displayed as grid")
def test_products_displayed_as_grid(remote_browser, base_url, logger_fixture):
    search_results_page = SearchResultsPage(remote_browser, base_url)
    logger_fixture.info("===== test_products_displayed_as_grid =====")
    search_results_page \
        .open(logger_fixture) \
        .click_display_as_grid() \
        .check_products_displayed_as_grid()
