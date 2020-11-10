from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Verify_locators import Locators2


class VerifyPage():

    def __init__(self, driver):
        self.driver = driver

        self.driver_dropdown_menu = Locators2.driver_dropdown_xpath
        self.driver_list = Locators2.driver_list_xpath
        self.driver_listview = Locators2.driver_listview_button_xpath

        self.verify_driver_name = Locators2.verify_drivername_xpath
        self.verify_driver_emailid = Locators2.verify_driver_email_id
        self.verify_nic = Locators2.verify_driver_nic_xpath
        self.vehicle_number = Locators2.verify_vehicle_number_xpath


    def click_on_driver_dropdown(self):
        self.driver.find_element(By.XPATH, self.driver_dropdown_menu).click()
    def click_on_driver_list(self):
        self.driver.find_element(By.XPATH, self.driver_list).click()
    def click_on_driver_listview(self):
        self.driver.find_element(By.XPATH, self.driver_listview).click()


    # def verify_driver_name(self):
    #     self.driver.find_element(By.XPATH, self.verify_driver_name)
    # def verify_email_id(self):
    #     self.driver.find_element(By.XPATH, self.verify_driver_emailid)
    # def verify_nic(self):
    #     self.driver.find_element(By.XPATH, self.verify_nic())
    # def verify_vehicle_number(self):
    #     self.driver.find_element(By.XPATH, self.vehicle_number)



