def test_search_results_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=product/search&search=iphone')
    browser.find_element_by_xpath("//h1[contains(text(), 'Search')]")
    browser.find_element_by_xpath("//h2[contains(text(), 'Search')]")
    browser.find_element_by_css_selector('input#input-search')
    browser.find_element_by_css_selector('select[name=category_id]')
    browser.find_element_by_css_selector('input[name=sub_category]')
    browser.find_element_by_css_selector('input#description')
    browser.find_element_by_css_selector('input#button-search')
