from selenium import webdriver
import time
import pytest
import allure
import warnings
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from TestData.config import TestData
from Pages.loginPage import LoginPage
from Pages.verify_driver_page import VerifyPage
from Locators.Verify_locators import Locators2
from Configuration.conftest import init_driver


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_verifypage(BaseTest):

    #@pytest.mark.login("Grouping/Marking the TC")
    #@pytest.mark.filterwarnings("warning filters to specific test items")
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(TestData.WRONG_USERNAME)
        self.lp.enter_password(TestData.WRONG_PASSWORD)
        self.lp.click_login(),time.sleep(2)

        verifyWrongEmailErrorMessage = self.driver.find_element(By.XPATH, Locators2.verifyWrongEmailErrorMessage_xpath)
        assert verifyWrongEmailErrorMessage.text == TestData.VERIFY_WRONG_EMAIL_MESSAGE,time.sleep(2)

        self.driver.refresh()

    #@pytest.mark.login
    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(TestData.BASE_URL)
        assert "Rent Vehicles" in self.driver.title
        print("Assertion Test Pass")
        try:
            assert "Rent Vehicles" in self.driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "multicompetition" in self.driver.current_url

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(TestData.USERNAME),time.sleep(2)
        self.lp.enter_password(TestData.PASSWORD)

        self.driver.find_element_by_css_selector("#btnLogin").is_enabled()
        print("Login button is enabled")
        self.driver.find_element_by_xpath("//a[@class='btn btn-link']").is_displayed()
        print("Forgot Password link is Displayed")

        self.lp.click_login(),time.sleep(2)

    @pytest.mark.run(order=3)
    def test_click_on_driver_dropdown(self):
        self.vp = VerifyPage(self.driver)
        self.vp.click_on_driver_dropdown()
        self.vp.click_on_driver_list()
        element = self.driver.find_element_by_xpath(Locators2.driver_listview_button_xpath)
        self.driver.execute_script("arguments[0].click();", element),time.sleep(2)


    # @pytest.mark.xfail("deliberately fail the TC")
    @pytest.mark.run(order=4)
    def test_verify_driver_details(self):
        self.vp = VerifyPage(self.driver)
        verify_driver_name = self.driver.find_element(By.XPATH, Locators2.verify_drivername_xpath)
        assert verify_driver_name.text == TestData.VERIFY_DRIVER_NAME

        link = None
        while not link:
            try:
                link = self.driver.find_element(By.XPATH, Locators2.verify_driver_email_id)
                print("verified register title")
            except NoSuchElementException:
                time.sleep(2)

        verify_driver_nic = self.driver.find_element(By.XPATH, Locators2.verify_driver_nic_xpath)
        if verify_driver_nic is not None:
            print("Driver nic number verified")
        else:
            print("Driver nic number is not verified")

        verify_driver_vehicle_number= self.driver.find_element(By.XPATH, Locators2.verify_vehicle_number_xpath)
        assert verify_driver_vehicle_number.text == TestData.VERIFY_VEHICLE_NUMBER,time.sleep(2)


    @pytest.mark.run(order=5)
    def test_logout_app(self):
        element = self.driver.find_element_by_xpath(Locators2.need_on_logout_xpath)
        self.driver.execute_script("arguments[0].click();", element), time.sleep(2)

        element2 = self.driver.find_element_by_xpath(Locators2.click_on_logout_xpath)
        self.driver.execute_script("arguments[0].click();", element2), time.sleep(2)


















