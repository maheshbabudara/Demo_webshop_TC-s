# from Lib.library import Base
# from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as e
#
# class practise(Base):
#     dropdown=('xpath',"//section[text()='Dropdown']")
#     country_locator=('xpath','//select[@id="select3"]')
#     login_locator=('xpath','//a[@class="ico-login"]')
#     un_locator=('xpath','//input[@id="Email"]')
#     pwd_locator=('xpath','//input[@id="Password"]')
#     login_btn=('xpath','//input[@value="Log in"]')
#
#     def prac(self):
#         self.click(self.dropdown)
#         self.drp_down(self.country_locator)
#
#     def driven(self,username,password):
#         self.click(self.login_locator)
#         sleep(1)
#         self.send_data(self.un_locator,username)
#         sleep(1)
#         self.send_data(self.pwd_locator,password)
#         sleep(1)
#         self.click(self.login_btn)
#

from Lib.lib2 import Base
from time import sleep

class prac(Base):
    searchbox_locator=('xpath','//input[@placeholder="Search for over 5000 products"]')
    unibic_cookies=('xpath',"//span[text()=' cookies']")
    Add_cart=('xpath',"//h5[text()='Unibic Cashew Badam Cookies']/../../..//div[@class='relative mt-12 px-1.5']//button[@data-testid='product-card-add-btn']/div/span")
    cart_locator=('xpath','//a[@aria-label="Cart"]')
    login_locator=('xpath','//h6[@class="block font-subtitle tracking-wider text-lg font-bold"]')
    phn_textbox=('xpath','//input[@placeholder="Enter Phone Number"]')
    continue_btn=('xpath',"//div[text()='Continue']")

    def mahe(self,text,phn_no):
        self.send_data(self.searchbox_locator,text)
        sleep(1)
        self.click(self.unibic_cookies)
        sleep(1)
        self.click(self.Add_cart)
        sleep(1)
        self.click(self.cart_locator)
        sleep(1)
        self.click(self.login_locator)
        sleep(1)
        self.send_data(self.phn_textbox,phn_no)
        sleep(2)
        self.click(self.continue_btn)
        sleep(10)


