import allure
import pytest
from allure_commons.types import AttachmentType
from POM.practise import practise
from time import sleep
from Utilities.Excelreader import reader

#Note: should not peform both Reday and write operations

# read=list_from_excel('Users.xlsx','test')
read=reader('pyframework_users.xlsx','test')

@pytest.mark.login
def test_practise(driver):
    p=practise(driver)
    p.prac()

@pytest.mark.login
@pytest.mark.parametrize('username,password',read)
def test_datadriven(data,username,password):
    d=practise(data)
    d.driven(username,password)
    condition=data.find_element('xpath','//a[@class="ico-logout"]').is_displayed()
    if condition==False:
        allure.attach(data.get_screenshot_as_png(),name='test_datadriven.png',attachment_type=AttachmentType.PNG)
    assert condition
