from pages.CatalogPage import CatalogPage


def test_catalog_page(browser, base_url):
    """
    Dz9. Just finding of elements on the catalog page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    # create catalog_page object
    catalog_page = CatalogPage(browser, base_url)
    # open page
    catalog_page.open()
    # find some elements on this page
    catalog_page.find_elements()
