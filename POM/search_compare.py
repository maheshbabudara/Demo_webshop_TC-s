from Lib.library import Base
from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver


class compare_searching(Base):
    Electronics_locator=('xpath','//ul[@class="top-menu"]//a[contains(text(),"Electronics")]')
    camera_photo_locator=('xpath','//ul[@class="sublist firstLevel active"]//a[contains(text(),"Camera, photo")]')
    Handycam_locator=('xpath','//a[text()="1MP 60GB Hard Drive Handycam Camcorder"]')
    Add_to_comparelist=('xpath','//input[@value="Add to compare list"]')
    Camrecorder_locator=('xpath','//a[text()="Camcorder"]')
    # remove_Cam_locator=('xpath','//input[@title="Remove"]')
    remove_Cam_locator = ('xpath', "//input[contains(@onclick,'/compareproducts/remove/20')]")
    Handy_locator = ('xpath', "//input[contains(@onclick,'/compareproducts/remove/44')]")

    def search_compare(self):
        self.Electronics_Hover(self.Electronics_locator)
        self.click_element(self.camera_photo_locator)
        self.click_element(self.Handycam_locator)
        self.click_element(self.Add_to_comparelist)
        self.Back()
        sleep(1)
        self.Back()
        self.click_element(self.Camrecorder_locator)
        self.click_element(self.Add_to_comparelist)
        sleep(1)
        self.click_element(self.remove_Cam_locator)
        sleep(1)
        self.click_element(self.Handy_locator)



