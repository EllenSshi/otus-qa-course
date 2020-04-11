from pages.MainPage import MainPage


def test_main_page(browser, base_url):
    """
    Dz9. Just finding of elements on the main page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    main_page = MainPage(browser, base_url)
    main_page\
        .open()\
        .check_featured_block_is_not_empty()
