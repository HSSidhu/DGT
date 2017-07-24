# -*- coding: utf-8 -*-
# Create First Call
# Book in Deceased
# Do the Mortuary Flow

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from POM.Helpers.LoginPage import LoginPage
from POM.Regression.BookingInPage import BookingInPage
from POM.Regression.MyUniqueID import MyUniqueID


class Automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("F:\\AUTOMATION\\Browsers\\Chrome\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next=/"
        self.verificationErrors = []
        self.accept_next_alert = True

#     def test_CreateNewCall(self):
#         driver = self.driver
#         driver.get(self.base_url + "/credentials/login/?next=/")
#
#         login= LoginPage(driver)
#         login.UserName("harwinder.sidhu@coopdigital.co.uk")
#         login.Password("password")
#         driver.find_element_by_id("djHideToolBarButton").click()
#
#         newfirstcall = FirstCallPage(driver)
#         newfirstcall.selectnewcall()
#         newfirstcall.setcallertitle("Mr")
#         newfirstcall.setcallerfirstname("Testing")
#         newfirstcall.setcallerlastname("User")
#         newfirstcall.setcallermainphone("0321313121133")
#         newfirstcall.setcallerotherphone("04324324324234")
#         newfirstcall.setrelationship("Aunt")
#         newfirstcall.setmaincontact()
#         newfirstcall.setfuneralhome("Colinton")
#         newfirstcall.setdeceasedtitle("Mr")
#         newfirstcall.setdeceasedfirstname("Testing")
#         newfirstcall.setdeceasedlastname("Data")
#         newfirstcall.setdeceasedgendermale()
#         newfirstcall.setdeceasedreligion("Other")
#         newfirstcall.setdeceasedDOB("01/01/1945")
#         newfirstcall.setdeceasedDOD("02/07/2017")
#         newfirstcall.setdeceasedCommitalburial()
#         newfirstcall.setcoronerinvolvedyes()
#         newfirstcall.setdeathverifiedyes()
#         newfirstcall.setdeathregisteredyes()
#         newfirstcall.setdeceasedPOD("Manchester")
#         newfirstcall.setcollectionreq()
#         newfirstcall.setresidence()
#         newfirstcall.setcollectionsame()
#         newfirstcall.setappointmentnow()
#         newfirstcall.savefirstcall()
#
# # FIRST CALL SAVED #
#
#         driver.find_element_by_link_text("Harry Kenyon").click()
#         referenceid = driver.find_element_by_id("deceased-reference").text

    def test_BookingIn(self):

        driver = self.driver
        driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/")

        login= LoginPage(driver)
        login.UserName("harwinder.sidhu@coopdigital.co.uk")
        login.Password("password")
        driver.find_element_by_id("djHideToolBarButton").click()

        # Unique ID function #
        uniquefunction = MyUniqueID(driver)
        UniqueID = uniquefunction.deceasedID("Harry Kenyon")

        # Booking Page #
        driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/tracking/")
        bookingin = BookingInPage(driver)
        bookingin.locationName("East Newington Place")

        # Login Page #
        #login= LoginPage(driver)
        login.UserName("edinburgh.fso@coopdigital.co.uk")
        login.Password("password")

        #driver.find_element_by_id("first_contact_id-204").click()
        #driver.find_elements(By.CLASS_NAME("tap-link__inner__title"),'//[text() = "Benny Dore"]').click()
        #driver.find_elements_by_class_name("tap-link__inner__title")
        # #driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]/span')
        # select_box = driver.find_elements_by_xpath(".//*[starts-with(@class,'tap-link__inner__title')]/span")
        # options = [x for x in select_box.find_elements_by_tag_name("Benny Dore")] #this part is cool, because it searches the elements contained inside of select_box and then adds them to the list options if they have the tag name "options"
        # for element in options:
        # print (element.get_attribute("value"))
        #for elem in driver.find_elements_by_xpath('.//span[@class = "icon icon-avatar"]'):
        #print (elem.get_attribute("innerHTML"))

        # Booking Page #
        bookingin = BookingInPage(driver)
        for elem in driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]'):
            if elem.text == "Harry Kenyon":
                ActionChains(driver).move_to_element(elem).click().perform()

                bookingin.Wristband()
                bookingin.DeceasedintoCare()
                bookingin.AllChecksComplete()

                driver.find_element_by_id("id_deceased_details-reference").send_keys(UniqueID)
                driver.find_element_by_id("goto_booking_in_done").click()
                driver.find_element_by_id("add-personal-effect").click()
                driver.find_element_by_id("id_personal_effect_form-description").send_keys("testing")
                driver.find_element_by_id("id_personal_effect_form-location").send_keys("testing")
                driver.find_element_by_id("id_personal_effect_form-client_instruction_2").click()
                driver.find_element_by_id("id_personal_effect_form-received_receipt_number").send_keys("312312")
                driver.find_element_by_id("goto_personal_effects_list").click()
                driver.find_element_by_id("goto_deceased_measurements").click()
                driver.find_element_by_id("id_deceased_measurements-height").send_keys("12")
                driver.find_element_by_id("id_deceased_measurements-width").send_keys("12")
                driver.find_element_by_id("id_deceased_measurements-depth").send_keys("21")
                driver.find_element_by_id("goto_deceased_location_assignment").click()

                Select(driver.find_element_by_id("id_deceased_location_assignment-location_assignment")).select_by_visible_text("East Newington Place - Holding Area (10)")

                driver.find_element_by_id("goto_deceased_notes").click()

                driver.find_element_by_id("id_deceased_notes-deceased_booking_notes").send_keys("Notes for the user")
                driver.find_element_by_id("goto_second_verification").click()

                driver.find_element_by_id("id_second_verification-second_user_email").send_keys("edinburgh.fd@coopdigital.co.uk")
                driver.find_element_by_id("id_second_verification-second_user_password").send_keys("password")
                driver.find_element_by_id("goto_booking_in_done").click()
                driver.find_element_by_id("id_second_deceased_details-completed_all_checks").click()
                driver.find_element_by_css_selector("label.tap-check").click()
                driver.find_element_by_id("goto_booking_in_done").click()
                driver.find_element_by_id("goto_welcome_screen").click()

                driver.quit()


        # driver.find_element_by_id("id_deceased_details-reference").send_keys(referenceid)
        #
        # driver.find_element_by_id("goto_booking_in_done").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
