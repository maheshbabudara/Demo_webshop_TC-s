import pytest
from POM.zepto_login import zepto_login
from time import sleep

@pytest.mark.login
def test_login(zepto):
    z=zepto_login(zepto)
    z.perform("8639563301")
    # assert zepto.find_element("xpath","//span[text()='profile']").is_displayed()

