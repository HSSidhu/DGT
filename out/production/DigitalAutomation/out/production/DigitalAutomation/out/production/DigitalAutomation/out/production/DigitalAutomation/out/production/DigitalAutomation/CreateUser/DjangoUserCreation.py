# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CreateUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("F:\\AUTOMATION\\Browsers\\Chrome\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/admin/login/?next=/admin"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_user(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("admin")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_id("djHideToolBarButton").click()
        driver.find_element_by_link_text("Users").click()
        #driver.find_element_by_link_text("Add user").click()
        driver.find_element_by_class_name("addlink").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("edinburgh.fso3@coopdigital.co.uk")
        driver.find_element_by_id("id_password1").clear()
        driver.find_element_by_id("id_password1").send_keys("Password1!")
        driver.find_element_by_id("id_password2").clear()
        driver.find_element_by_id("id_password2").send_keys("Password1!")
        driver.find_element_by_id("id_staffmember-0-uuid").clear()
        driver.find_element_by_id("id_staffmember-0-uuid").send_keys("12345654767")
        driver.find_element_by_id("id_staffmember-0-staff_id_number").clear()
        driver.find_element_by_id("id_staffmember-0-staff_id_number").send_keys("98777777")
        Select(driver.find_element_by_id("id_staffmember-0-primary_site")).select_by_visible_text("Colinton")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-secondary_sites | label=Lothian Road]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-capabilities | label=can_conduct_funeral]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-capabilities | label=can_schedule_resources]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-capabilities | label=can_view_security_audit]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-capabilities | label=can_administer_scheduler_settings]]
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_staffmember-0-capabilities | label=can_administer_users]]
        driver.find_element_by_id("id_staffmember-0-primary_mobile_number").clear()
        driver.find_element_by_id("id_staffmember-0-primary_mobile_number").send_keys("0342424324324")
        driver.find_element_by_id("id_staffmember-0-contracted_hours_per_week").clear()
        driver.find_element_by_id("id_staffmember-0-contracted_hours_per_week").send_keys("37.50")
        driver.find_element_by_name("_continue").click()
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("edinburgh")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("fso3")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("edinburgh.fso2@coopdigital.co.uk")
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | id=id_groups | label=funeral_director]]
        driver.find_element_by_name("_continue").click()
        driver.find_element_by_name("_save").click()
        driver.find_element_by_link_text("Log out").click()

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
