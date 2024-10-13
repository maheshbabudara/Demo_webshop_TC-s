from Lib.library import Base
from time import sleep


class cart(Base):
    apparel_shoes_locator=('xpath','//ul[@class="top-menu"]//a[@href="/apparel-shoes"]')
    Belt_Add_locator=('xpath','//a[text()="Casual Golf Belt"]/../..//div[@class="add-info"]//div[@class="buttons"]//input[@value="Add to cart"]')
    popup_shopping_cart=('xpath',"//a[text()='shopping cart']")
    quantity_textbox=('xpath','//input[@class="qty-input"]')
    update_button=('xpath','//input[@value="Update shopping cart"]')
    remove_checkbox=('xpath','//input[@name="removefromcart"]')
    message_cary=('xpath','//div[@class="order-summary-content"]')

    def shoe(self,text):
        self.click_element(self.apparel_shoes_locator)
        sleep(2)
        self.click_element(self.Belt_Add_locator)
        sleep(2)
        self.click_element(self.popup_shopping_cart)
        sleep(2)
        self.clear_data(self.quantity_textbox)
        sleep(2)
        self.send_data(self.quantity_textbox,text)
        sleep(2)
        self.click_element(self.update_button)
        sleep(3)
        self.click_element(self.remove_checkbox)
        sleep(2)
        self.click_element(self.update_button)

