from PageObjects.locators import HomePage, CreateAccountTab, PaymentTab, ShoppingCartPage, PageHeader, MyAccountPage
from SeleniumBase.WebActions import Selenium
from selenium.common.exceptions import NoSuchElementException
import time


class HomePageFunctions(Selenium):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.get_url(url)

    def hover_on_dreses_menu(self, option_name):
        self.hover_on_locator(HomePage._dresses_menu_option(option_name))

    def select_option(self, option_name):
        self.click_element(HomePage._dresses_menu_option(option_name))

    def set_quantity(self, quantity):
        self.enter_text(HomePage._item_quantity, quantity)

    def select_size(self, size):
        self.select_by_text(HomePage._item_size, size)

    def select_color(self, color):
        self.click_element(HomePage._item_color(color))

    def click_add_to_cart(self):
        self.click_element(HomePage._add_to_cart)

    def click_continue_to_shopping(self):
        self.scroll_down()
        self.click_element(HomePage._continue_to_shopping)

    def search_dress(self, search_dress):
        elements = self.find_elements(HomePage._product_name)
        try:
            for element in elements:
                if element.text == search_dress:
                    self.scroll_to_element(element)
                    self.hover_on_element(element)
                    index = elements.index(element)
                    self.find_from_elements(
                        HomePage._on_hover_add_to_cart, index).click()
                    self.click_element(HomePage._proceed_to_checkout)
                    break
        except UnexpectedAlertPresentException:
            self.dismiss_browser_alert()
            self.click_element(HomePage._proceed_to_checkout)
            pass
        except NoSuchElementException:
            print('No Such Product')
            pass

    def proceed_to_checkout(self):
        try:
            self.scrollToElement(ShoppingCartPage._proceed_to_checkout)
            self.click_element(ShoppingCartPage._proceed_to_checkout)
        except UnexpectedAlertPresentException:
            self.dismiss_browser_alert()
            pass

    def proceed_to_create_account(self, email_to_enter):
        self.explicitly_wait_for_time(5)
        self.enter_text(
            CreateAccountTab._create_account_email_field, email_to_enter)
        self.click_element(CreateAccountTab._create_account_button)

    def fill_mandatory_fields(self, name, password, phone_number, zip_code, state):
        # for sake of testing using same data in places,
        # in real time need to be precise about test data
        self.wait_for_is_displayed(CreateAccountTab._create_account_first_name)
        self.explicitly_wait_for_time(3)
        self.enter_text(CreateAccountTab._create_account_first_name, name)
        self.enter_text(CreateAccountTab._create_account_last_name, name)
        self.enter_text(CreateAccountTab._create_account_address, name)
        self.enter_text(CreateAccountTab._create_account_city, name)
        self.wait_for_is_displayed(CreateAccountTab._create_account_state)
        self.select_by_text(CreateAccountTab._create_account_state, state)
        self.enter_text(CreateAccountTab._create_account_zipcode, zip_code)
        self.enter_text(CreateAccountTab._create_account_mobile, zip_code+zip_code)
        self.enter_text(CreateAccountTab._create_account_password, password)

        self.click_element(CreateAccountTab._create_account_register_button)
        self.click_element(CreateAccountTab._proceed_to_checkout_from_adress_tab)

    def check_terms_and_contition_box(self):
        self.click_element(CreateAccountTab._terms_and_condition)
        self.click_element(CreateAccountTab._proceed_to_checkout_from_shipping_tab)

    def pay_by_bank_wire(self):
        self.click_element(PaymentTab._bank_wire_method)
        self.click_element(PaymentTab._i_confirm_button)

    def save_reference_number(self):
        return self.get_text(PaymentTab._reference_text)

    def navigate_to_order_history(self):
        self.click_element(PageHeader._my_profile_option)
        self.click_element(MyAccountPage._order_and_details)

    def get_order_price(self):
        return self.get_text(MyAccountPage._order_details_price)

    def get_order_reference_number(self):
        return self.get_text(MyAccountPage._order_details_reference_number)

    def sign_out(self):
        self.click_element(PageHeader._sign_out)

    def decrease_quantity(self, dress_name, quantity_decrease_by):
        for index in range(quantity_decrease_by):
            self.click_element(ShoppingCartPage._quantity_decrease_icon(dress_name))
