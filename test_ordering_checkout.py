from Manager.PageInstace import ClassInstance
from Utils.RandamData import Utils


class Test_Ordering(ClassInstance):

    def test_order_checkout(self):
        email = '%s@gmail.com' % Utils._get_random_alphanumeric_string()
        name = Utils._get_random_alphabetic_string()
        phone_number = Utils._get_random_numeric_string()
        zip_code = Utils._get_random_five_number_string()
        password = Utils._get_random_five_number_string()
        state = 'California'

        self.get_home_page().open('http://automationpractice.com/')
        self.get_home_page().hover_on_dreses_menu('Dresses')
        self.get_home_page().select_option('Evening Dresses')
        self.get_home_page().select_option('Printed Dress')
        self.get_home_page().set_quantity('2')
        self.get_home_page().select_size('L')
        self.get_home_page().select_color('Pink')
        self.get_home_page().click_add_to_cart()
        self.get_home_page().click_continue_to_shopping()
        self.get_home_page().select_option('Women')
        self.get_home_page().search_dress('Printed Chiffon Dress')
        self.get_home_page().decrease_quantity('Printed Dress', 1)
        self.get_home_page().proceed_to_checkout()
        self.get_home_page().proceed_to_create_account(email)
        self.get_home_page().fill_mandatory_fields(
            name, password, phone_number, zip_code, state)
        self.get_home_page().check_terms_and_contition_box()
        self.get_home_page().pay_by_bank_wire()

        order_details = self.get_home_page().save_reference_number()

        self.get_home_page().navigate_to_order_history()

        assert self.get_home_page().get_order_price() in order_details
        assert self.get_home_page().get_order_reference_number() in order_details

        self.get_home_page().sign_out()
