import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
location=os.getcwd()

@pytest.fixture
def driver():
    driver=WebDriver()
    option=Options()
    option.add_experimental_option('detach',True)
    option.add_argument('--disable-Notification')
    preferences={'download.default_director':location,'pluins.always_open_pdf_externally':True}
    option.add_experimental_option('prefs',preferences)
    driver.get("https://demoapps.qspiders.com/ui?scenario=1")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()

@pytest.fixture
def data():
    data=WebDriver()
    data.get("https://demowebshop.tricentis.com/")
    data.implicitly_wait(10)
    data.maximize_window()
    yield data
    data.close()

@pytest.fixture()
def zepto():
    zepto=WebDriver()
    option=Options()
    option.add_argument("--disable-Notifications")
    zepto.get("https://www.zeptonow.com/search")
    zepto.implicitly_wait(10)
    zepto.maximize_window()
    yield zepto
    zepto.close()

