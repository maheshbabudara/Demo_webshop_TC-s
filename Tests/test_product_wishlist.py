import allure
from allure_commons.types import AttachmentType

from POM.product_wishlist import product_wishlist
from time import sleep

def test_product_wishlist(wishlist):
    p=product_wishlist(wishlist)
    p.wish('0')
    condition=wishlist.find_element('xpath','//div[@class="wishlist-content"]').is_displayed()
    if condition==False:
        allure.attach(wishlist.get_screenshot_as_png(),name="test_product_wishlist.png",attachment_type=AttachmentType.PNG)
    assert condition
