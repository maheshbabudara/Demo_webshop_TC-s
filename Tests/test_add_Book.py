from time import sleep

import allure
from allure_commons.types import AttachmentType

from POM.Books_Add_to_cart import Books

def test_Add_Book(Book):
    b=Books(Book)
    b.addtocart()
    condition=Book.find_element('xpath','//td[@class="product"]//a[text()="Computing and Internet"]').is_displayed()
    if condition==False:
        allure.attach(Book.get_screenshot_as_png(),name='test_add_Book.png',attachment_type=AttachmentType.PNG)
    assert condition