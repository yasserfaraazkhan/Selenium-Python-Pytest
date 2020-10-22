from WebPages.HomePage import *
from configuration.BaseClass import *

class ClassInstance(BaseClass):
    home_page = None
    payment_page = None

    def get_home_page(self):
        if self.home_page == None:
            self.home_page = HomePageFunctions(self.getDriver())
        return self.home_page
