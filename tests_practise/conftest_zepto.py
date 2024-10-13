import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys

@pytest.fixture
def zepto():
    zepto=WebDriver()
    option=Options()
    option.add_argument("--disable-Notifications")
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    zepto.get("https://www.zeptonow.com/")
    sleep(1)
    zepto.maximize_window()
    zepto.implicitly_wait(10)
    yield zepto
    zepto.close()
