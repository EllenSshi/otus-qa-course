from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, 'img#user-profile')


class AdminLoginPageLocators:
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input#input-username')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#input-password')
    FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, 'a[href*=forgotten]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[type=submit]')
    FOOTER = (By.CSS_SELECTOR, '#footer')
    INVALID_AUTH_MSG = (By.XPATH, "//div[contains(text(), 'No match for Username and/or Password')]")


class MainPageLocators:
    SLIDESHOW = (By.CSS_SELECTOR, 'div#slideshow0')
    SLIDESHOW_PAGINATION = (By.CSS_SELECTOR, '.swiper-pagination.slideshow0')
    FEATURED_BLOCK = (By.XPATH, "//h3[contains(text(), 'Featured')]")
    CAROUSEL = (By.CSS_SELECTOR, 'div#carousel0')
    CAROUSEL_PAGINATION = (By.CSS_SELECTOR, '.swiper-pagination.carousel0')
    FEATURED_BLOCK_IMAGES = (By.CSS_SELECTOR, '.image')
    FEATURED_BLOCK_CAPTIONS = (By.CSS_SELECTOR, '.caption')
    FEATURED_BLOCK_BTN_GROUPS = (By.CSS_SELECTOR, '.button-group')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div ~ h1')
    THUMBNAILS = (By.CSS_SELECTOR, '.thumbnails')
    DESC_AND_REVIEW_TABS = (By.CSS_SELECTOR, '.nav-tabs')
    DESCRIPTION_TAB = (By.PARTIAL_LINK_TEXT, 'Description')
    REVIEW_TAB = (By.PARTIAL_LINK_TEXT, 'Reviews')
    REVIEW_NAME_INPUT = (By.CSS_SELECTOR, '#input-name')
    REVIEW_TEXT_INPUT = (By.CSS_SELECTOR, '#input-review')
    REVIEW_RATING_MARKS = (By.CSS_SELECTOR, 'input[name=rating]')
    REVIEW_BTN = (By.CSS_SELECTOR, '#button-review')
    TAB_CONTENT = (By.CSS_SELECTOR, '.tab-content')
    QUANTITY_INPUT = (By.CSS_SELECTOR, 'input#input-quantity')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button#button-cart')
    RATING = (By.CSS_SELECTOR, 'div.rating')
    ALERTS = (By.CSS_SELECTOR, '.alert')
    COMPARE_BTN = (By.CSS_SELECTOR, 'button[data-original-title="Compare this Product"]')
    COMPARISON_LINK = (By.LINK_TEXT, 'product comparison')


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
    LIST_BTN = (By.CSS_SELECTOR, 'button#list-view')
    GRID_BTN = (By.CSS_SELECTOR, 'button#grid-view')
    LIST_PRODUCTS = (By.CSS_SELECTOR, 'div.product-list')
    GRID_PRODUCTS = (By.CSS_SELECTOR, 'div.product-grid')


class AdminProductsPageLocators:
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
    RANDOM_PRODUCT = (By.CSS_SELECTOR, 'tbody tr')
    RANDOM_PRODUCT_NAME = (By.CSS_SELECTOR, 'tbody tr > td:nth-child(3)')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Delete"]')


class AdminAddAndEditProductPageLocators:
    PRODUCT_NAME_INPUT = (By.CSS_SELECTOR, 'input#input-name1')
    META_TAG_TITLE_INPUT = (By.CSS_SELECTOR, 'input#input-meta-title1')
    DATA_TAB = (By.CSS_SELECTOR, 'a[href="#tab-data"]')
    MODEL_INPUT = (By.CSS_SELECTOR, 'input#input-model')
    PRICE_INPUT = (By.CSS_SELECTOR, 'input#input-price')
    QUANTITY_INPUT = (By.CSS_SELECTOR, 'input#input-quantity')
    SAVE_BTN = (By.CSS_SELECTOR, 'button[type=submit]')
    IMAGE_TAB = (By.CSS_SELECTOR, 'a[href="#tab-image"]')
    IMAGE = (By.CSS_SELECTOR, 'a#thumb-image')
    EDIT_IMAGE_BTN = (By.CSS_SELECTOR, 'button#button-image')
    UPLOAD_BTN = (By.CSS_SELECTOR, 'button#button-upload')
    IMAGE_INPUT = (By.CSS_SELECTOR, 'input[type=file]')
    CLOSE_BTN = (By.CSS_SELECTOR, 'button.close')


class ComparisonPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, 'table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) strong')
