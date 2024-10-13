from Lib.library import Base
from time import sleep

class product_review(Base):
    Jewelery_locator=('xpath','//ul[@class="top-menu"]//a[@href="/jewelry"]')
    price_range=('xpath','//span[text()="0.00"]')
    product_name=('xpath',"//a[text()='Black & White Diamond Heart']")
    Add_review=('xpath',"//a[text()='Add your review']")
    review_title=('xpath','//input[@name="AddProductReview.Title"]')
    review_textarea=('xpath','//textarea[@name="AddProductReview.ReviewText"]')
    rating_box=('xpath','//input[@id="addproductrating_4"]')
    submit_review=('xpath','//input[@value="Submit review"]')

    def review(self,title,textarea):
        self.click_element(self.Jewelery_locator)
        sleep(2)
        self.click_element(self.price_range)
        sleep(2)
        self.click_element(self.product_name)
        sleep(2)
        self.click_element(self.Add_review)
        sleep(2)
        self.send_data(self.review_title,title)
        sleep(2)
        self.send_data(self.review_textarea,textarea)
        sleep(2)
        self.click_element(self.rating_box)
        sleep(2)
        self.click_element(self.submit_review)

