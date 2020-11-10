from selenium.webdriver.common.by import By
from Locators.Locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.dropdown_xpath = Locators.dropdown_xpath
        self.select_registerdriver_xpath = Locators.select_registerdriver_xpath

    def click_dropdown_menu(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def select_registerdriver_page(self):
        self.driver.find_element(By.XPATH, self.select_registerdriver_xpath).click()



