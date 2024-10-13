import allure
import pytest
from allure_commons.types import AttachmentType

from POM.product_review import product_review
from time import sleep

@pytest.mark.review
def test_pro_review(Review):
    r=product_review(Review)
    r.review('Diamond H','Good product worth for money')
    condition=Review.find_element('xpath','//div[@class="rest"]').is_displayed() and Review.find_element('xpath','//div[@class="review-title"]/strong[text()="Diamond H"]').is_displayed()
    if condition==False:
        allure.attach(Review.get_screenshot_as_png(),name='test_Product_Review.png',attachment_type=AttachmentType.PNG)
    assert condition