from Lib.lib2 import Base
from time import sleep
from Utilities.locators import loc
class zepto_login(Base):
    def perform(self,phn_no):
        self.click(loc.login_btn)
        sleep(1)
        self.send_data(loc.input_text,phn_no)
        sleep(1)
        self.click(loc.continue_btn)
        sleep(10)
        self.click(loc.cart_icon)
        sleep(2)
        self.remove_Multi_items(loc.remove_items)
        sleep(2)
