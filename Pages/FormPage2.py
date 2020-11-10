from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from selenium.webdriver.support.select import Select

class FormPage2():

    def __init__(self, driver):
        self.driver = driver

        self.upload_vehicle_registration_copy_xpath  = Locators.vehicle_registration_copy_xpath
        self.upload_driver_photo_xpath = Locators.driver_photo_xpath
        self.enter_parking_location_xpath  = Locators.parking_location_xpath

        self.hiring_time_from_name = Locators.hiring_time_from_name
        self.hiring_time_to_name = Locators.hiring_time_to_name
        self.select_hiring_location_name = Locators.prefer_hiring_location_name
        self.submit_button_id = Locators.submit_sutton_id


    def upload_vehicle_registration_copy(self, vehicle_registration_copy):
        #print("test messge")
        self.driver.find_element(By.XPATH, self.upload_vehicle_registration_copy_xpath).send_keys(vehicle_registration_copy)


    def upload_driver_photo(self, driver_photo):
        self.driver.find_element(By.XPATH, self.upload_driver_photo_xpath).send_keys(driver_photo)

    def enter_parking_location(self, parking_location):
        self.driver.find_element(By.XPATH, self.enter_parking_location_xpath).send_keys(parking_location)


    def enter_prefer_hiring_from(self, hiring_from):
        self.driver.find_element(By.NAME, self.hiring_time_from_name).send_keys(hiring_from)

    def enter_prefer_hiring_to(self, hiring_to):
        self.driver.find_element(By.NAME, self.hiring_time_to_name).send_keys(hiring_to)

    def select_prefer_hiring_location(self, prefer_location):
        element = self.driver.find_element(By.NAME, self.select_hiring_location_name)
        sel2 = Select(element)
        sel2.select_by_index(1)

    def click_submit_button(self, submit):
        self.driver.find_element(By.NAME, self.submit_button_id).click()



























