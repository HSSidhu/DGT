import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from POM.CalendarPage import CalendarPage
from POM.MyUniqueID import MyUniqueID


class AdminLoginPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def local(self):
        self.driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("admin")

    def preprod(self):
        self.driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("PX3TfHt5JxW72mJnpdG7Yr4S")

    def qa(self):
        self.driver.get ("https://funeral-director-frontend-qa.fnc-dev.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin@admin.com")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("admin")
        
        