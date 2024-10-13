from Lib.library import Base
from time import sleep

class product_wishlist(Base):
    apparel_shoes_locator=('xpath','//ul[@class="top-menu"]//a[@href="/apparel-shoes"]')
    Display_drp=('xpath','//select[@name="products-pagesize"]')
    product_name=('xpath',"//a[text()='Blue and green Sneaker']")
    Add_to_wishlist=('xpath','//input[@value="Add to wishlist"]')
    popup_wishlist=('xpath',"//a[text()='wishlist']")
    quantity_textbpx=('xpath','//input[@class="qty-input"]')
    update_btn=('xpath','//input[@value="Update wishlist"]')

    def wish(self,text):
        self.click_element(self.apparel_shoes_locator)
        sleep(2)
        self.display_dropdown_4(self.Display_drp)
        sleep(2)
        self.display_dropdown_8(self.Display_drp)
        sleep(2)
        self.display_dropdown_12(self.Display_drp)
        sleep(2)
        self.click_element(self.product_name)
        sleep(2)
        self.click_element(self.Add_to_wishlist)
        sleep(2)
        self.click_element(self.popup_wishlist)
        sleep(2)
        self.clear_data(self.quantity_textbpx)
        sleep(2)
        self.send_data(self.quantity_textbpx,text)
        sleep(3)
        self.click_element(self.update_btn)


