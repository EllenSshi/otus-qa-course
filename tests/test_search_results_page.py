from pages.SearchResultsPage import SearchResultsPage


def test_search_results_page(browser, base_url):
    """
    Dz9. Just finding of elements on the search results page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create search_results_page object
    search_results_page = SearchResultsPage(browser, base_url)
    # open page
    search_results_page.open()
    # find some elements on this page
    search_results_page.find_elements()
