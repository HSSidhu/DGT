import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from POM.AutomationDriver import AutomationDriver


class MyUniqueID(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def deceasedID(self, deceasedname):
        self.driver.find_element_by_link_text(deceasedname).click()
        referenceid = AutomationDriver.driver.find_element_by_id("deceased-reference").text
        unique = referenceid.split(':')[1].strip()
        return unique
