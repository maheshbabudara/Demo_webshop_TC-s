import allure
from allure_commons.types import AttachmentType

from POM.Query import user_query


def test_query(quer):
    u=user_query(quer)
    u.query('Issue with my Login')
    condition=quer.find_element('xpath','//div[@class="result"]').is_displayed()
    if condition==False:
        allure.attach(quer.get_screenshot_as_png(),name="test_query.png",attachment_type=AttachmentType.PNG)
    assert condition
