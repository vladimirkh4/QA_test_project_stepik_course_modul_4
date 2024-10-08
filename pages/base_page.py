from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # метод для вызова методов содержащих assert с обработкой исключений
    # используется для корректной работы метода run_test_with_multy_methods
    def call_function_with_try_exception(self, func):
        try:
            func()
        except NoSuchElementException:
            print(f'No search element for {func} function')
            return 1
        except AssertionError as err:
            print(err)
            return 1

        return 0

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    # метод для запуска методов содержащих несколько последовательных проверок с использованием assert
    # нужен для того чтобы при выбросе исключения одной из проверок, отработали все последующие проверки
    # после отработки всех проверок, если хотя бы одна заквершилась исключением,
    # метод выбрасывает исключение ValueError c информацией о количестве проверок завершившихся неудачно
    def run_test_with_multy_methods(self, methods_list):
        check_counter = 0
        for method in methods_list:
            check_method = self.call_function_with_try_exception(method)
            check_counter += check_method

        if check_counter > 0:
            raise ValueError(f"QUANTITY FAILED TESTS: {check_counter} FROM {len(methods_list)}")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON),\
            "User icon is not presented,probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),\
            "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")