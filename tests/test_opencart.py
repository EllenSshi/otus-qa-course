def test_app(browser, base_url):
    browser.get(base_url + "/opencart/")
    assert browser.title == "Your Store"
