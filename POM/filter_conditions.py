from Lib.library import Base
from time import sleep

class filter(Base):
    computer_locator=('xpath','//ul[@class="top-menu"]//a[@href="/computers"]')
    desktop_locator=('xpath','//ul[@class="top-menu"]//a[@href="/desktops"]')
    sort_locator=('xpath','//select[@name="products-orderby"]')
    display_locator=('xpath','//select[@name="products-pagesize"]')
    under_1k_locator=('xpath','//a[@href="https://demowebshop.tricentis.com/desktops?orderby=11&pagesize=4&price=-1000"]')
    remove_filter_locator=('xpath',"//a[text()='Remove Filter']")
    range_price_locator=('xpath','//a[@href="https://demowebshop.tricentis.com/desktops?orderby=11&pagesize=4&price=1000-1200"]')
    above_1k_locator=('xpath','//a[@href="https://demowebshop.tricentis.com/desktops?orderby=11&pagesize=4&price=1200-"]')

    def fil(self):
        self.computer_hover(self.computer_locator)
        sleep(2)
        self.click_element(self.desktop_locator)
        sleep(2)
        self.sort_AtoZ(self.sort_locator)
        sleep(4)
        self.sort_ZtoA(self.sort_locator)
        sleep(4)
        self.sort_lowtohigh(self.sort_locator)
        sleep(4)
        self.sort_hightolow(self.sort_locator)
        sleep(4)
        self.display_4(self.display_locator)
        sleep(4)
        self.click_element(self.under_1k_locator)
        sleep(4)
        self.click_element(self.remove_filter_locator)
        sleep(1)
        self.click_element(self.range_price_locator)
        sleep(4)
        self.click_element(self.remove_filter_locator)
        sleep(2)
        self.click_element(self.above_1k_locator)
        sleep(4)



