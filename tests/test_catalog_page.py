def test_catalog_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=product/category&path=20')
    browser.find_element_by_css_selector('.list-group')
    browser.find_element_by_css_selector('button#list-view')
    browser.find_element_by_css_selector('button#grid-view')
    browser.find_element_by_css_selector('a#compare-total')
    browser.find_element_by_css_selector('select#input-sort')
    browser.find_element_by_css_selector('select#input-limit')
