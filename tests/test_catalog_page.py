import allure
from pages.CatalogPage import CatalogPage


@allure.title("Main page")
def test_catalog_page(remote_browser, base_url, logger_fixture):
    """
    Dz9. Just finding of elements on the catalog page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_catalog_page =====")
    # create catalog_page object
    catalog_page = CatalogPage(remote_browser, base_url)
    # open page
    catalog_page.open(logger_fixture)
    # find some elements on this page
    catalog_page.find_elements()
