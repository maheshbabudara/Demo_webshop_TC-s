from Lib.library import Base
from time import sleep

class email(Base):
    Electronics_locator=('xpath','//ul[@class="top-menu"]//a[@href="/electronics"]')
    cellphones_locator=('xpath','//ul[@class="top-menu"]//a[@href="/cell-phones"]')
    smartphone_locator=('xpath',"//a[text()='Smartphone']")
    Email_friend=('xpath','//input[@value="Email a friend"]')
    frnd_email_textbox=('xpath','//input[@id="FriendEmail"]')
    # emailid_textbox=('xpath','//input[@id="YourEmailAddress"]')
    personal_msg_textarea=('xpath','//textarea[@name="PersonalMessage"]')
    sendmail_btn=('xpath','//input[@value="Send email"]')

    def frnd_email(self,mail,message):
        self.Electronics_Hover(self.Electronics_locator)
        sleep(2)
        self.click_element(self.cellphones_locator)
        sleep(2)
        self.click_element(self.smartphone_locator)
        sleep(2)
        self.click_element(self.Email_friend)
        sleep(2)
        self.send_data(self.frnd_email_textbox,'abc')
        sleep(2)
        self.clear_data(self.frnd_email_textbox)
        sleep(2)
        self.click_element(self.sendmail_btn)
        sleep(2)
        self.send_data(self.frnd_email_textbox,mail)
        sleep(2)
        # self.send_data(self.emailid_textbox,mailid)
        sleep(2)
        self.send_data(self.personal_msg_textarea,message)
        sleep(2)
        self.click_element(self.sendmail_btn)

