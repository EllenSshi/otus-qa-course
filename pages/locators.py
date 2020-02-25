from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#input-password')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href*=forgotten]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type=submit]')
    FOOTER = (By.CSS_SELECTOR, '#footer')


class MainPageLocators:
    SLIDESHOW = (By.CSS_SELECTOR, 'div#slideshow0')
    SLIDESHOW_PAGINATION = (By.CSS_SELECTOR, '.swiper-pagination.slideshow0')
    FEATURED_BLOCK = (By.XPATH, "//h3[contains(text(), 'Featured')]")
    CAROUSEL = (By.CSS_SELECTOR, 'div#carousel0')
    CAROUSEL_PAGINATION = (By.CSS_SELECTOR, '.swiper-pagination.carousel0')


class ProductPageLocators:
    THUMBNAILS = (By.CSS_SELECTOR, '.thumbnails')
    DESC_AND_REVIEW_TABS = (By.CSS_SELECTOR, '.nav-tabs')
    TAB_CONTENT = (By.CSS_SELECTOR, '.tab-content')
    QUANTITY_INPUT = (By.CSS_SELECTOR, 'input#input-quantity')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button#button-cart')
    RATING = (By.CSS_SELECTOR, 'div.rating')


class CatalogPageLocators:
    LIST_GROUP = (By.CSS_SELECTOR, '.list-group')
    LIST_BTN = (By.CSS_SELECTOR, 'button#list-view')
    GRID_BTN = (By.CSS_SELECTOR, 'button#grid-view')
    COMPARE_LINK = (By.CSS_SELECTOR, 'a#compare-total')
    SORT_INPUT = (By.CSS_SELECTOR, 'select#input-sort')
    SHOW_INPUT = (By.CSS_SELECTOR, 'select#input-limit')


class SearchResultsPageLocators:
    PRODUCT_SEARCH_BLOCK = (By.XPATH, "//h1[contains(text(), 'Search')]")
    SEARCH_RESULTS = (By.XPATH, "//h2[contains(text(), 'Search')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input#input-search')
    CATEGORY_SELECT = (By.CSS_SELECTOR, 'select[name=category_id]')
    SUB_CATEGORY_CHECKBOX = (By.CSS_SELECTOR, 'input[name=sub_category]')
    SEARCH_IN_DESCRIPTION_CHECKBOX = (By.CSS_SELECTOR, 'input#description')
    SEARCH_BTN = (By.CSS_SELECTOR, 'input#button-search')