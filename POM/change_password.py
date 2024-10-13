from Lib.library import Base
from time import sleep

class password(Base):
    myaccount_locator=('xpath',"//a[text()='My account']")
    change_pwd_locator=('xpath',"//a[text()='Change password']")
    old_pwd_locator=('xpath','//input[@name="OldPassword"]')
    new_pwd_locator=('xpath','//input[@name="NewPassword"]')
    confirm_pwd_locator=('xpath','//input[@name="ConfirmNewPassword"]')
    change_pwd_btn=('xpath','//input[@value="Change password"]')
    logout_locator=('xpath','//a[text()="Log out"]')
    login_locator=('xpath','//a[@href="/login"]')
    Emailid_locator=('id','Email')
    password_locator=('xpath','//input[@id="Password"]')
    submit_login_locator=('xpath','//div[@class="buttons"]//input[@value="Log in"]')

    def pwd(self,old_pwd,new_pwd,confirm_pwd,emailid,password_text):
        self.click_element(self.myaccount_locator)
        sleep(2)
        self.click_element(self.change_pwd_locator)
        sleep(2)
        self.send_data(self.old_pwd_locator,old_pwd)
        sleep(2)
        self.send_data(self.new_pwd_locator,new_pwd)
        sleep(2)
        self.send_data(self.confirm_pwd_locator,confirm_pwd)
        sleep(2)
        self.click_element(self.change_pwd_btn)
        sleep(2)
        self.click_element(self.logout_locator)
        sleep(2)
        self.click_element(self.login_locator)
        sleep(2)
        self.send_data(self.Emailid_locator,emailid)
        sleep(2)
        self.send_data(self.password_locator,password_text)
        sleep(2)
        self.click_element(self.submit_login_locator)
        