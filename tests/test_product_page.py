def test_admin_login_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=product/product&product_id=40')
    browser.find_element_by_css_selector('.thumbnails')
    browser.find_element_by_css_selector('.nav-tabs')
    browser.find_element_by_css_selector('.tab-content')
    browser.find_element_by_css_selector('div#product')
    browser.find_element_by_css_selector('input#input-quantity')
    browser.find_element_by_css_selector('button#button-cart')
    browser.find_element_by_css_selector('div.rating')
