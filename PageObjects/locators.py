from selenium.webdriver.common.by import By

class PageHeader():
    _my_profile_option = {"by": By.CLASS_NAME, "value": "account"}
    _sign_out = {"by": By.CLASS_NAME, "value": "logout"}

class MyAccountPage():
    _order_and_details = {"by": By.XPATH, "value": "//*[contains(@title,'Orders')]"}
    _order_details_reference_number = {"by": By.CLASS_NAME, "value": "color-myaccount"}
    _order_details_price = {"by": By.CLASS_NAME, "value": "history_price"}

class HomePage():
    _dresses_menu_option= lambda dress_name: {"by": By.XPATH, "value": "(//a[@title='%s'])[2]" % dress_name}
    _item_quantity = {"by": By.ID, "value": "quantity_wanted"}
    _item_size = {"by": By.ID, "value": "group_1"}
    _item_size = {"by": By.ID, "value": "group_1"}
    _add_to_cart = {"by": By.ID, "value": "add_to_cart"}
    _item_color = lambda _item_color: {"by": By.XPATH, "value": "//a[@name='%s']" % _item_color}
    _continue_to_shopping = {"by": By.XPATH, "value": "//span[@title='Continue shopping']"}
    _product_name = {"by": By.XPATH, "value": "//h5[@itemprop='name']"}
    _on_hover_add_to_cart = {"by": By.XPATH, "value": "//a[@title='Add to cart']"}
    _proceed_to_checkout = {"by": By.XPATH, "value": "//a[@title='Proceed to checkout']"}

class ShoppingCartPage():
    _quantity_decrease_icon = lambda dress_name: {"by": By.XPATH, "value": "//p[@class='product-name']/a[contains(text(), '%s')]/ancestor::tr/descendant::td/descendant::a[contains(@class,'button-minus')]" % dress_name}
    _proceed_to_checkout = {"by": By.XPATH, "value": "(//a[@title='Proceed to checkout'])[2]"}

class CreateAccountTab():
    _create_account_email_field = {"by": By.ID, "value": "email_create"}
    _create_account_button = {"by": By.ID, "value": "SubmitCreate"}
    _create_account_first_name = {"by": By.ID, "value": "customer_firstname"}
    _create_account_last_name = {"by": By.ID, "value": "customer_lastname"}
    _create_account_password = {"by": By.ID, "value": "passwd"}
    _create_account_address = {"by": By.ID, "value": "address1"}
    _create_account_city = {"by": By.ID, "value": "city"}
    _create_account_state = {"by": By.ID, "value": "id_state"}
    _create_account_zipcode = {"by": By.ID, "value": "postcode"}
    _create_account_country = {"by": By.ID, "value": "id_country"}
    _create_account_mobile = {"by": By.ID, "value": "phone_mobile"}
    _create_account_adress_future_reference = {"by": By.ID, "value": "alias"}
    _create_account_register_button = {"by": By.ID, "value": "submitAccount"}
    _terms_and_condition = {"by": By.ID, "value": "cgv"}
    _proceed_to_checkout_from_adress_tab = {"by": By.NAME, "value": "processAddress"}
    _proceed_to_checkout_from_shipping_tab = {"by": By.NAME, "value": "processCarrier"}

class PaymentTab():
    _bank_wire_method = {"by": By.CLASS_NAME, "value": "bankwire"}
    _i_confirm_button = {"by": By.XPATH, "value": "//*[contains(text(),'I confirm my order')]"}
    _final_total_cost = {"by": By.XPATH, "value": "//*[contains(@class,'price')]/strong"}
    _reference_text = {"by": By.XPATH, "value": "//*[contains(@class,'box')]"}
