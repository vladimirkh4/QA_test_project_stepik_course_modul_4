from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    LANGUAGE = (By.CSS_SELECTOR, '[name="language"] [selected="selected"]')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content #content_inner .row')
    MESSAGE_ABOUT_EMPTY = (By.CSS_SELECTOR, '.content #content_inner p')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    PASSWORD_REPEAT = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():

    BASKET_ADD = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    NAME_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
