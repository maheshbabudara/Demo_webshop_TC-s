from Lib.library import Base
from time import sleep

class advance(Base):
    search_option=('xpath','//a[text()="Search"]')
    searchbar_locator=('xpath','//input[@class="search-text"]')
    searchbox_check=('xpath','//div[@class="inputs reversed"]//input[@id="As"]')
    category_dropdown=('xpath','//select[@id="Cid"]')
    search_btn=('xpath','//div[@class="buttons"]//input[@value="Search"]')
    logout_btn=('xpath','//a[text()="Log out"]')

    def advance_search_call(self,text):
        self.click_element(self.search_option)
        self.send_data(self.searchbar_locator,text)
        self.click_element(self.searchbox_check)
        self.category_computers(self.category_dropdown)
        self.click_element(self.search_btn)
        sleep(2)
        self.category_shoe(self.category_dropdown)
        self.click_element(self.search_btn)

    def advance_search_computer(self,text):
        self.click_element(self.search_option)
        self.send_data(self.searchbar_locator,text)
        self.click_element(self.searchbox_check)
        self.category_computers(self.category_dropdown)
        self.click_element(self.search_btn)







