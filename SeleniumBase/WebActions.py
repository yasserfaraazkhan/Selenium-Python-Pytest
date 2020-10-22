from configuration.BaseClass import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, \
    InvalidElementStateException
import time
from selenium.webdriver.common.action_chains import ActionChains


class Selenium(BaseClass):
    driver = None
    _timeout = 10

    def __init__(self, driver):
        self.driver = self.getDriver()

    def _highlight(self, element):
        def apply_style(style):
            self.driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);", element, style)
        apply_style("background: yellow; border: 2px solid red;")
        return element

    def find_element(self, locator):
        return self._highlight(self.driver.find_element(locator["by"], locator["value"]))

    def get_text(self, locator):
        return self.find_element(locator).text

    def find_elements(self, locator):
        return self.driver.find_elements(locator["by"], locator["value"])

    def enter_text(self, locator, input_string):
        self.wait_for_is_displayed(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(input_string)
        # self.find_element(locator).send_keys(Keys.RETURN)

    def click_element(self, locator):
        self.wait_for_is_clickable(locator)
        self.driver.find_element(locator["by"], locator["value"]).click()

    def scrollToElement(self, locator):
        self.getDriver().execute_script(
            "arguments[0].scrollIntoView();", self.find_element(locator))

    def click_from_dropdown(self, locator, text):
        result_elements = self.find_elements(locator)
        for i in result_elements:
            if i.text == text:
                i.click()
                break

    # get a particular element from list of elements
    def find_from_elements(self, locator, index):
        return self.find_elements(locator)[index]

    def hover_on_locator(self, locator):
        hover = ActionChains(self.getDriver()).move_to_element(
            self.find_element(locator))
        hover.perform()

    def hover_on_element(self, element):
        hover = ActionChains(self.getDriver()).move_to_element(element)
        hover.perform()

    def select_by_text(self, locator, text):
        select = Select(self.find_element(locator))
        select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        select = Select(self.find_element(locator))
        select.select_by_value(value)

    def get_url(self, url):
        self.driver.get(url)

    def wait_for_is_clickable(self, locator):
        try:
            wait = WebDriverWait(self.getDriver(), self._timeout)
            if type(locator) is dict:
                wait.until(EC.element_to_be_clickable(
                    (locator['by'], locator['value'])))
            else:
                wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def wait_for_is_displayed_after(self, locator, timeout):
        try:
            wait = WebDriverWait(self.getDriver(), timeout)
            wait.until(EC.visibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True

    def wait_for_is_displayed(self, locator):
        self.wait_for_is_displayed_after(locator, self._timeout)

    def wait(self, seconds):
        time.sleep(seconds)

    def wait_till_alert_present_and_assert(self, alert_message):
        try:
            wait = WebDriverWait(self.getDriver(), self._timeout)
            wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            assert alert.text == alert_message
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print("no alert")
            assert False

    def scroll_to_element(self, element):
        # element = self.find_element(locator)
        x = element.location['x']
        y = element.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
        self.driver.execute_script(scroll_by_coord)
        self.driver.execute_script(scroll_nav_out_of_way)

    def scroll_down(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def dismiss_browser_alert(self):
        wait = WebDriverWait(self.getDriver(), self._timeout)
        wait.until(EC.alert_is_present(), "The alert was not displayed")
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def explicitly_wait_for_time(self, time_to_wait_sec):
        time.sleep(time_to_wait_sec)
