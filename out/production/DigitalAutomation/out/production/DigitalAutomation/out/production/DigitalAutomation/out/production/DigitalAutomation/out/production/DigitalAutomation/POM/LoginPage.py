import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginPage(object):

    def __init__(self,AutomationDriver):
         self.driver= AutomationDriver

    def UserName(self, UserName):
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys(UserName)

    def Password(self, Password):
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys(Password)
        self.driver.find_element_by_xpath("//input[@value='Login']").click()


