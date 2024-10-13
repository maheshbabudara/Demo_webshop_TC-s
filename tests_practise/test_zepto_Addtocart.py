import allure
import pytest
from allure_commons.types import AttachmentType
from POM.practise import prac
from time import sleep


@pytest.mark.zepto
def test_zepto_cart(zepto):
    p=prac(zepto)
    p.mahe('unibic','8639563301')
    condition=zepto.find_element('xpath',"//p[text()='Unibic Cashew Badam Cookies']").is_displayed()
    if condition==False:
        allure.attach(zepto.get_screenshot_as_png(),name="test_zepto_cart.png",attachment_type=AttachmentType.PNG)
    assert condition
