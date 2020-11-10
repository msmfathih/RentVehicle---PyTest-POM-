import time
import pytest
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from Configuration.conftest import init_driver
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.FormPage import FormPage
from Pages.FormPage2 import FormPage2
from TestData.config import TestData


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_loginpage(BaseTest):

    def test_login(self):
        self.driver.get(TestData.BASE_URL)
        self.driver.implicitly_wait(10)

        assert "Rent Vehicles" in self.driver.title
        print("Assertion Test Pass")
        try:
            assert "Rent Vehicles" in self.driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "multicompetition" in self.driver.current_url

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(TestData.USERNAME)
        self.lp.enter_password(TestData.PASSWORD)

        verifyForgotPassword = self.driver.find_element(By.XPATH, Locators.forgot_password_xpath)
        assert verifyForgotPassword.text == Locators.forgot_password_message

        self.lp.click_login()

    def test_homepage(self):
        self.hp = HomePage(self.driver)
        self.hp.click_dropdown_menu()
        self.hp.select_registerdriver_page()
        # self.driver.execute_script("window.scrollBy(0,1000)", "")


    def test_fillform(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_drivername(TestData.DRIVER_NAME),time.sleep(2)
        self.ff.enter_mobile_number(TestData.DRIVER_MOBILE_NUMBER),time.sleep(2)
        self.ff.enter_email(TestData.DRIVER_EMAIL),time.sleep(2)
        self.ff.enter_driver_password(TestData.DRIVER_PASSWORD),time.sleep(2)
        self.ff.enter_nic(TestData.DRIVER_NIC),time.sleep(2)


    def test_upload_licenece_copy_file(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_licence(TestData.FILE_UPLOAD_PATH),time.sleep(2)


    def test_upload_licenece_backcopy_file(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_licence_back(TestData.FILE_UPLOAD_BACK_PATH),time.sleep(2)

    def test_priority6_enter_vehicle_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_vehicle_number(TestData.VEHICLE_NUMBER)



    def test_vehicle_owner_radiobtn(self):
        element = self.driver.find_element_by_css_selector("input.is_vehicle_owner:nth-child(4)")
        self.driver.execute_script("arguments[0].click();", element)


    def test_select_vehicle_type(self):
        self.ff = FormPage(self.driver)
        self.ff.select_vehicle_type(Locators.select_vehicle_type_xpath)
        self.driver.execute_script("window.scrollBy(0,500)", "")


    def test_upload_vehicle_picture(self):
        self.ff = FormPage(self.driver)
        self.ff.upload_vihicle_picture(TestData.FILE_UPLOAD_VEHICLE_PICTURE)

    def test_enter_engine_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_engine_number(TestData.ENGINE_NUMBER)

    def test_enter_chassis_number(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_chassis_number(TestData.CHASSIS_NUMBER)

    def test_hiring_times(self):
        self.ff = FormPage(self.driver)
        self.ff.enter_prefer_hiring_from(TestData.HIRING_TIME_FROM)
        self.ff.enter_prefer_hiring_to(TestData.HIRING_TIME_TO)

    def test_upload_driver_registration(self):
        self.fp = FormPage2(self.driver)
        self.fp.upload_vehicle_registration_copy(TestData.FILE_UPLOAD_VEHICLE_REGISTRATION_COPY)

    def test_upload_driver_photo(self):
        self.fp = FormPage2(self.driver)
        self.fp.upload_driver_photo(TestData.FILE_UPLOAD_DRIVER_PHOTO)

    def test_enter_parking_location(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_parking_location(TestData.PARKING_LOCATION)

    def test_enter_hiring_location_from(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_prefer_hiring_from(TestData.HIRING_TIME_FROM)

    def test_enter_hiring_location_to(self):
        self.fp = FormPage2(self.driver)
        self.fp.enter_prefer_hiring_to(TestData.HIRING_TIME_TO)

    def test_select_hiring_location(self):
        self.fp = FormPage2(self.driver)
        self.fp.select_prefer_hiring_location(Locators.parking_location_xpath)

    def test_submit_details(self):
        element = self.driver.find_element_by_id("submitBtn")
        self.driver.execute_script("arguments[0].click();", element)

        verifyEmailId = self.driver.find_element(By.XPATH, Locators.verify_already_existing_email_xpath)
        assert verifyEmailId.text == TestData.EMAIL_VALIDATION































