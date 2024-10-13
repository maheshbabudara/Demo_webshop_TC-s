import allure
from allure_commons.types import AttachmentType

from POM.change_password import password
from time import sleep

def test_change_password(chng_pwd):
    p=password(chng_pwd)
    p.pwd('selenium','test123','test123','reddyvinuth27@gmail.com','test123')
    condition=chng_pwd.find_element('xpath',"//a[text()='reddyvinuth27@gmail.com']").is_displayed()
    if condition==False:
        allure.attach(chng_pwd.get_screenshot_as_png(),name='test_change_password.png',attachment_type=AttachmentType.PNG)
    assert condition
    