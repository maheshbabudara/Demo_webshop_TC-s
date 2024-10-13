import allure
import pytest
from allure_commons.types import AttachmentType
from POM.search_compare import compare_searching
from time import sleep

@pytest.mark.compare
def test_compare(compare):
    c=compare_searching(compare)
    c.search_compare()
    condition=compare.find_element('xpath','//div[contains(@class,"page-body")]').is_displayed()
    if condition ==False:
        allure.attach(compare.get_screenshot_as_png(),name='test_compare_search.png',attachment_type=AttachmentType.PNG)
    assert True

