def test_app(browserstack_browser):
    browserstack_browser.get("http://yandex.ru")
    browserstack_browser.find_element_by_css_selector("input#text")
