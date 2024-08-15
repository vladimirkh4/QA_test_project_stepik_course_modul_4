from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class ProductPageLocators():

    BASKET_ADD = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")