from pages.locators import ProductPageLocators


def test_product_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=product/product&product_id=40')
    browser.find_element(*ProductPageLocators.THUMBNAILS)
    browser.find_element(*ProductPageLocators.DESC_AND_REVIEW_TABS)
    browser.find_element(*ProductPageLocators.TAB_CONTENT)
    browser.find_element(*ProductPageLocators.QUANTITY_INPUT)
    browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
    browser.find_element(*ProductPageLocators.RATING)
