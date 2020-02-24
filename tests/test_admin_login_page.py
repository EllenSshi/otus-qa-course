def test_admin_login_page(browser, base_url):
    browser.get(base_url + '/opencart/admin/')
    browser.find_element_by_css_selector('input#input-username')
    browser.find_element_by_css_selector('input#input-password')
    browser.find_element_by_css_selector('a[href*=forgotten]')
    browser.find_element_by_css_selector('button[type=submit]')
    browser.find_element_by_css_selector('#footer')
