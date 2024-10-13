# from time import sleep
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
#
# class Base:
#     def __init__(self,driver):
#         self.driver=driver
#         self.action=ActionChains(self.driver)
#
#     def search_element(self,locator):
#         element=self.driver.find_element(*locator)
#         return element
#
#     # def search_elements(self,locator):
#     #     elements=self.driver.find_elements(*locator)
#     #     return elements
#
#     def click_element(self,locator):
#         ele=self.search_element(locator)
#         ele.click()
#
#     def send_data(self,locator,text):
#         ele=self.search_element(locator)
#         ele.send_keys(text)
#
#     def clear_data(self,locator):
#         ele=self.search_element(locator)
#         ele.clear()
#
#     def category_computers(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text("Computers")
#     def category_shoe(self,locator):
#         drp_down=Select(self.search_element(locator))
#         drp_down.select_by_visible_text('Apparel & Shoes')
#
#     def Electronics_Hover(self,locator):
#         ele=self.search_element(locator)
#         self.action.move_to_element(ele).perform()
#     def Back(self):
#         b=self.driver
#         b.back()
#     def display_dropdown_4(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text("4")
#     def display_dropdown_8(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text("8")
#
#     def display_dropdown_12(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text("12")
#
#     def country_drp(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text("India")
#     def state_drp(self,locator):
#         drp=Select(self.search_element(locator))
#         drp.select_by_visible_text('Other (Non US)')
#
#     def alert_pop(self):
#         pop=self.driver.switch_to.alert
#         pop.accept()
#
#     def computer_hover(self,locator):
#         ele=self.search_element(locator)
#         self.action.move_to_element(ele).perform()
#
#     def sort_AtoZ(self,locator):
#         ele=Select(self.search_element(locator))
#         ele.select_by_visible_text("Name: A to Z")
#
#     def sort_ZtoA(self,locator):
#         ele=Select(self.search_element(locator))
#         ele.select_by_visible_text("Name: Z to A")
#
#     def sort_lowtohigh(self,locator):
#         ele=Select(self.search_element(locator))
#         ele.select_by_visible_text("Price: Low to High")
#
#     def sort_hightolow(self,locator):
#         ele=Select(self.search_element(locator))
#         ele.select_by_visible_text("Price: High to Low")
#
#     def display_4(self,locator):
#         ele=Select(self.search_element(locator))
#         ele.select_by_visible_text("4")
#
#
#
#
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e



class Base:
    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)
    def search_element(self,locator):
        # element=WebDriverWait(self.driver,10,ignored_exceptions=[NoSuchElementException,
        #                                                  ElementNotVisibleException,
        #                                                  ElementNotSelectableException,
        #                                                  Exception],poll_frequency=0.2).until(
        #     e.visibility_of_element_located(*locator)
        # )
        # return element
        element=self.driver.find_element(*locator)
        return element

    def click_element(self,locator):
        ele=self.search_element(locator)
        ele.click()
    def send_data(self,locator,text):
        ele=self.search_element(locator)
        ele.send_keys(text)
    def double_click(self,locator):
        ele=self.search_element(locator)
        self.action.double_click(ele).perform()
    def drp_down(self,locator):
        ele=Select(self.search_element(locator))
        # ele.select_by_visible_text("name")
        values=ele.options
        for item in values:
            if item.text=="Germany":
                item.click()


