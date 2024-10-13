import allure
from allure_commons.types import AttachmentType

from POM.shoppingcart_conditions import cart
from time import sleep

def test_shopping(cart_condition):
    c=cart(cart_condition)
    c.shoe('4')
    condition=cart_condition.find_element('xpath','//div[@class="order-summary-content"]').is_displayed()
    if condition==False:
        allure.attach(cart_condition.get_screenshot_as_png(),name='test_cartcondition.png',attachment_type=AttachmentType.PNG)
    assert condition
