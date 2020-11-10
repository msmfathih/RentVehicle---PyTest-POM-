class Locators2():

    #login page objects
    username_textbox_id = "email"
    password_textbox_id = "password"
    loginbtn_id = "btnLogin"
    verifyWrongEmailErrorMessage_xpath = "//strong[contains(text(),'These credentials do not match our records.')]"

    # home page objects
    driver_dropdown_xpath = "/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a"
    driver_list_xpath = "//p[contains(text(),'Drivers List')]"
    driver_listview_button_xpath  = "//tbody/tr[8]/td[6]/a[1]"


    #driver list view
    verify_drivername_xpath = "//label[contains(text(),'Driver Name : aadil')]"
    verify_driver_email_id = "//label[contains(text(),'Email : fazil@gmail.com')]"
    verify_driver_nic_xpath = "//label[contains(text(),'NIC Number: 920012213V')]"
    verify_vehicle_number_xpath = "//label[contains(text(),'Vehicle Number : EP-HQ-8165')]"
    verify_vehicle_type_xpath  = "//label[contains(text(),'Vehicle Number : EP-HQ-8165')]"

    #logout
    need_on_logout_xpath = "//p[contains(text(),'Need to logout ?')]"
    click_on_logout_xpath ="//p[contains(text(),'Logout')]"



