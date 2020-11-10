class Locators():

    #login page objects
    username_textbox_id = "email"
    password_textbox_id = "password"
    loginbtn_id = "btnLogin"
    forgot_password_xpath = "//a[contains(text(),'Forgot Your Password?')]"
    forgot_password_message = "Forgot Your Password?"

    #home page objects
    dropdown_xpath = "/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a"
    select_registerdriver_xpath = "//p[contains(text(),'Register Drivers')]"


    #enter form details
    drivername_xpath = "//input[@name='name']"
    mobile_number_xpath = "//input[@name='mobile_number']"
    email_xpath = "//input[@name='email']"
    password_xpath = "//input[@name='password']"
    nic_xpath = "//input[@name='nic']"

    #enter form details2
    licenece_copy_file_id = "name"
    licenece_backcopy_file_xpath = "//div[@class='content-wrapper']//div[7]//input[1]"
    vehicle_number_xpath = "//input[@name='vehicle_number']"

    #enter form details3 radiobtn and dropdown menu
    select_vehicle_owner_css_selector  = "input.is_vehicle_owner:nth-child(4)"
    select_vehicle_owner_permission_xpath = "//select[@name='owner_id']"
    select_vehicle_type_xpath = "//select[@name='vehicle_type_id']"


    #upload picture of vehicle
    picture_vehicle_xpath = "//input[@name='vehicle_picture']"
    engine_number_xpath = "//input[@name='engine_number']"
    chassis_number_xpath = "//input[@name='chassis_number']"
    vehicle_registration_copy_xpath = "//input[@name='vehicle_registration_copy']"
    driver_photo_xpath  = "//input[@name='photo']"
    parking_location_xpath = "//input[@name='parking_location']"

    hiring_time_from_name = "prefer_time_from"
    hiring_time_to_name = "prefer_time_to"
    prefer_hiring_location_name = "prefer_location_to_hire"

    submit_sutton_id = "submitBtn"
    verify_already_existing_email_xpath = "/html/body/div[1]/div[1]/section/div/div[1]/form/div/div[1]/div/strong"





