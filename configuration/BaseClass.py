import sys, pytest
from selenium.webdriver.support.ui import WebDriverWait
import config

@pytest.mark.usefixtures("setup")
class BaseClass():

    wait = None
    url = None

    def getDriver(self):
        return self.driver

    def getWait(self):
        if self.wait is None:
            self.wait = WebDriverWait(self.getDriver(), 10)
        return self.wait

    def setUp(self):
        print ("in setUp method")
        self.verificationErrors = []
        self.accept_next_alert = True
        print ("Current Test: " + self._testMethodName)

    def tearDown(self):
        "Tear down the test"
        print ("In tearDown")
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            self.driver.save_screenshot("%s.png" % test_method_name)
