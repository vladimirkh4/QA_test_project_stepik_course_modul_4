from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def only_add_product_to_basket(self):
        self.should_be_button_for_add_to_basket()

        button_add_basket = self.browser.find_element(*ProductPageLocators.BASKET_ADD)
        button_add_basket.click()
        self.solve_quiz_and_get_code()

    def add_product_to_basket_with_check_basket(self):
        self.should_be_button_for_add_to_basket()

        button_add_basket = self.browser.find_element(*ProductPageLocators.BASKET_ADD)
        button_add_basket.click()
        self.solve_quiz_and_get_code()

        check_list = [self.should_be_massage_about_add_to_basket,
                      self.should_be_massage_with_price_basket,
                      self.should_be_name_book_in_page,
                      self.should_be_price_book_in_page,
                      self.check_name_book_in_basket,
                      self.check_price_basket]

        self.run_test_with_multy_methods(check_list)

    def should_be_button_for_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD),\
            "Button for add to basket is not presented"

    def should_be_massage_about_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BOOK_IN_BASKET),\
            "Massage about add to basket is not presented"

    def should_be_massage_with_price_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET),\
            "Massage with price basket is not presented"

    def should_be_name_book_in_page(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BOOK),\
            "Name book is not presented on this page"

    def should_be_price_book_in_page(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BOOK),\
            "Price book is not presented on this page"

    def check_name_book_in_basket(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET).text
        assert name_book == name_book_in_basket,\
            f"Book name '{name_book}' is no equal book name in basket '{name_book_in_basket}'"

    def check_price_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert book_price == basket_price,\
            f"Book price '{book_price}' is no equal basket price '{basket_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_BOOK_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_BOOK_IN_BASKET), \
            "Success message should be disappeared, but it is presented"


