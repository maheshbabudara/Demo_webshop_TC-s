from Lib.library import Base
from time import sleep

class user_query(Base):
    contactus_option=('xpath',"//a[text()='Contact us']")
    enquiryarera_text=('xpath','//textarea[@name="Enquiry"]')
    submit_btn=('xpath','//input[@name="send-email"]')

    def query(self,text):
        self.click_element(self.contactus_option)
        sleep(2)
        self.send_data(self.enquiryarera_text,text)
        sleep(2)
        self.click_element(self.submit_btn)
