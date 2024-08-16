from .base_page import BasePage
from .locators import BasketPageLocators, BasePageLocators


class BasketPage(BasePage):
    MESSAGES_DICT = {'ru': 'Ваша корзина пуста',
                     'uk': 'Ваш кошик пустий.',
                     'en-gb': 'Your basket is empty.',
                     'es': 'Tu carrito esta vacío.',
                     'fr': 'Votre panier est vide.',
                     'it': 'Il tuo carrello è vuoto.',
                     'fi': 'Korisi on tyhjä',
                     'de': 'Ihr Warenkorb ist leer.'}

    def check_basket_with_multy_methods(self):
        check_list = [self.should_not_be_product_in_basket,
                      self.should_be_message_about_basket_empty,
                      self.check_message_about_basket_empty_for_ru_content]

        self.run_test_with_multy_methods(check_list)

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Products is presented in basket, but should not be"

    def should_be_message_about_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY),\
            "Message about basket epmty is not presented"

    def check_message_about_basket_empty_for_ru_content(self):
        message = self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY).text
        language = self.browser.find_element(*BasePageLocators.LANGUAGE).get_attribute('value')
        frase_about_basket_empty = self.MESSAGES_DICT.get(language, 'Your basket is empty.')

        assert frase_about_basket_empty in message,\
            f"Message({message}) no content '{frase_about_basket_empty}'"