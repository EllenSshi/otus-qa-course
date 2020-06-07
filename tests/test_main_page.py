import allure
from pages.MainPage import MainPage


@allure.title("Main page")
def test_main_page(remote_browser, base_url, logger_fixture):
    """
    Dz9. Just finding of elements on the main page
    :param browser: fixture from conftest.py
    :param base_url: fixture from conftest.py
    """
    logger_fixture.info("===== test_main_page =====")
    main_page = MainPage(remote_browser, base_url)
    main_page\
        .open(logger_fixture)\
        .check_featured_block_is_not_empty()
