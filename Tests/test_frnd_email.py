import allure
from allure_commons.types import AttachmentType

from POM.Email_freind import email
from time import sleep

def test_frnd_email(friend):
    f=email(friend)
    f.frnd_email('mail2mahebabu@gmail.com','Hello Mahesh')
    condition=friend.find_element('xpath','//div[@class="result"]').is_displayed()
    if condition==False:
        allure.attach(friend.get_screenshot_as_png(),name="test_frnd_email.png",attachment_type=AttachmentType.PNG)
    assert condition
