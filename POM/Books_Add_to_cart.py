from Lib.library import Base
from time import  sleep


class Books(Base):
    Books_locator=('xpath','//ul[@class="top-menu"]//a[contains(text(),"Books")]')
    Book_title_locator=('xpath','//h2[@class="product-title"]//a[text()="Computing and Internet"]')
    Addcart_locator=('xpath','//div[@class="add-to-cart-panel"]//input[@value="Add to cart"]')
    shopping_cart_locator=('xpath','//span[text()="Shopping cart"]')


    def addtocart(self):
        self.click_element(self.Books_locator)
        sleep(2)
        self.click_element(self.Book_title_locator)
        sleep(2)
        self.click_element(self.Addcart_locator)
        sleep(2)
        self.click_element(self.shopping_cart_locator)
        sleep(1)
