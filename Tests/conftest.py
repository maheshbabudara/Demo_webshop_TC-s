import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
import os
location=os.getcwd()
from time import sleep


@pytest.fixture
def advancesearch():
    advancesearch=WebDriver()
    option=Options()
    option.add_experimental_option('detach',True)
    option.add_argument('--disable-Notifications')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    preferences={'download.default_directory':location,'plugins.always_open_pdf_externally':True}
    option.add_experimental_option('prefs',preferences)
    advancesearch.get("https://demowebshop.tricentis.com/")
    advancesearch.implicitly_wait(10)
    advancesearch.maximize_window()
    advancesearch.find_element('xpath','//a[text()="Log in"]').click()
    sleep(1)
    advancesearch.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    advancesearch.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    advancesearch.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield advancesearch
    advancesearch.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture
def advance_invalid():
    advance_invalid=WebDriver()
    option=Options()
    option.add_experimental_option('detach',True)
    option.add_argument('--disable-Notifications')
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    preferences={'download.default_directory':location,'plugins.always_open_pdf_externally':True}
    option.add_experimental_option('prefs',preferences)
    advance_invalid.get("https://demowebshop.tricentis.com/")
    advance_invalid.implicitly_wait(10)
    advance_invalid.maximize_window()
    advance_invalid.find_element('xpath','//a[text()="Log in"]').click()
    sleep(1)
    advance_invalid.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    advance_invalid.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    advance_invalid.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield advance_invalid
    advance_invalid.find_element('xpath','//a[text()="Log out"]').click()


@pytest.fixture
def compare():
    compare=WebDriver()
    compare.get("https://demowebshop.tricentis.com/")
    compare.implicitly_wait(10)
    compare.maximize_window()
    sleep(1)
    compare.find_element('xpath','//a[@href="/login"]').click()
    sleep(1)
    compare.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    compare.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    compare.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield compare
    compare.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture
def Book():
    Book=WebDriver()
    option=Options()
    option.add_argument('--disable-Notifications')
    option.add_experimental_option('detach',True)
    Book.get("https://demowebshop.tricentis.com/")
    Book.implicitly_wait(10)
    Book.maximize_window()
    sleep(1)
    Book.find_element('xpath','//a[@href="/login"]').click()
    sleep(1)
    Book.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    Book.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    Book.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield Book
    Book.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture
def cart_condition():
    cart_condition=WebDriver()
    option=Options()
    cart_condition.get("https://demowebshop.tricentis.com/")
    cart_condition.implicitly_wait(10)
    cart_condition.maximize_window()
    sleep(1)
    cart_condition.find_element('xpath','//a[@href="/login"]').click()
    sleep(1)
    cart_condition.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    cart_condition.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    cart_condition.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield cart_condition
    cart_condition.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture
def wishlist():
    wishlist=WebDriver()
    option=Options()
    option.add_argument('--disable-Notifications')
    option.add_experimental_option('detach',True)
    wishlist.get("https://demowebshop.tricentis.com/")
    wishlist.implicitly_wait(10)
    wishlist.maximize_window()
    sleep(1)
    wishlist.find_element('xpath','//a[@href="/login"]').click()
    sleep(1)
    wishlist.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    wishlist.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    wishlist.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    yield wishlist
    wishlist.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture
def Review():
    Review=WebDriver()
    option=Options()
    option.add_experimental_option('detach',True)
    option.add_argument('--disable-Notifications')
    Review.get("https://demowebshop.tricentis.com/")
    Review.implicitly_wait(10)
    Review.maximize_window()
    Review.find_element('xpath','//a[@href="/login"]').click()
    sleep(1)
    Review.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(1)
    Review.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(1)
    Review.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(1)
    yield Review
    Review.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture()
def friend():
    friend=WebDriver()
    option=Options()
    friend.get("https://demowebshop.tricentis.com/")
    friend.implicitly_wait(10)
    friend.maximize_window()
    friend.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    friend.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    friend.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    friend.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield friend
    friend.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture()
def addres():
    addres=WebDriver()
    option=Options()
    addres.get("https://demowebshop.tricentis.com/")
    addres.implicitly_wait(10)
    addres.maximize_window()
    addres.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    addres.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    addres.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    addres.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield addres
    # addres.find_element('xpath','//a[text()="Log out"]').click()


@pytest.fixture()
def chng_pwd():
    chng_pwd=WebDriver()
    option=Options()
    chng_pwd.get("https://demowebshop.tricentis.com/")
    chng_pwd.implicitly_wait(10)
    chng_pwd.maximize_window()
    chng_pwd.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    chng_pwd.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    chng_pwd.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    chng_pwd.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield chng_pwd
    chng_pwd.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture()
def quer():
    quer=WebDriver()
    option=Options()
    quer.get("https://demowebshop.tricentis.com/")
    quer.implicitly_wait(10)
    quer.maximize_window()
    quer.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    quer.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    quer.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    quer.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield quer
    quer.find_element('xpath','//a[text()="Log out"]').click()

@pytest.fixture()
def fil_con():
    fil_con=WebDriver()
    option=Options()
    fil_con.get("https://demowebshop.tricentis.com/")
    fil_con.implicitly_wait(10)
    fil_con.maximize_window()
    fil_con.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    fil_con.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    fil_con.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    fil_con.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield fil_con
    fil_con.find_element('xpath','//a[text()="Log out"]').click()


@pytest.fixture()
def Buy_product():
    Buy_product=WebDriver()
    option=Options()
    Buy_product.get("https://demowebshop.tricentis.com/")
    Buy_product.implicitly_wait(10)
    Buy_product.maximize_window()
    Buy_product.find_element('xpath','//a[@href="/login"]').click()
    sleep(2)
    Buy_product.find_element('id','Email').send_keys('reddyvinuth27@gmail.com')
    sleep(2)
    Buy_product.find_element('xpath','//input[@id="Password"]').send_keys('selenium')
    sleep(2)
    Buy_product.find_element('xpath','//div[@class="buttons"]//input[@value="Log in"]').click()
    sleep(2)
    yield Buy_product
    Buy_product.find_element('xpath','//a[text()="Log out"]').click()




    










