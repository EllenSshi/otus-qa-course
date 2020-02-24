def test_main_page(browser, base_url):
    browser.get(base_url + '/opencart/index.php?route=common/home')
    browser.find_element_by_css_selector('div#slideshow0')
    browser.find_element_by_css_selector('.swiper-pagination.slideshow0')
    browser.find_element_by_xpath("//h3[contains(text(), 'Featured')]")
    browser.find_element_by_css_selector('div.swiper-viewport')
    browser.find_element_by_css_selector('.swiper-pagination.carousel0')
