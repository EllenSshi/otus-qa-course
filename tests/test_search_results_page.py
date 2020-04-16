from pages.SearchResultsPage import SearchResultsPage


def test_products_display(browser, base_url, logger_fixture):
    """
    Dz9. Just finding of elements on the search results page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_products_display =====")
    search_results_page = SearchResultsPage(browser, base_url)
    search_results_page\
        .open(logger_fixture)\
        .click_display_as_list()\
        .check_products_displayed_as_list()

    search_results_page \
        .open(logger_fixture) \
        .click_display_as_grid() \
        .check_products_displayed_as_grid()
