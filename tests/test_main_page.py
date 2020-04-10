from pages.CatalogPage import CatalogPage


def test_main_page(browser, base_url):
    """
    Dz9. Just finding of elements on the main page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create main_page object
    main_page = CatalogPage(browser, base_url)
    # open page
    main_page.open()
    # find some elements on this page
    main_page.find_elements()
