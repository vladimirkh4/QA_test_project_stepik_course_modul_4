import pytest
from time import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

head = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{head}{num}" for num in range(10)]
links[7] = pytest.param(links[7], marks=pytest.mark.xfail)


@pytest.mark.guest_add_to_basket_parametrize
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.check_form_with_multy_message_about_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link, 1)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_with_multy_methods()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:
    LINK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time()) + "@fakemail.org"
        password = 'Stepik_4_3'
        page = LoginPage(browser, self.LINK)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.LINK, 1)
        page.open()
        page.should_not_be_success_message()
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.LINK)
        page.open()
        page.check_form_with_multy_message_about_add_to_basket()
        page.should_be_authorized_user()
