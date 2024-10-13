from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def search_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def elements(self,locator) :
        elements=self.driver.find_elements(*locator)
        return elements
    def click(self,locator):
        ele=self.search_element(locator)
        return ele.click()
    def send_data(self,locator,text):
        ele=self.search_element(locator)
        ele.send_keys(text)
    def double(self,locator):
        ele=self.search_element(locator)
        self.action.double_click(ele).perform()
    def remove_Multi_items(self,locator):
        ele=self.elements(locator)
        for i in ele:
            i.click()









