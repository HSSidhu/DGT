import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TrackingApp(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def local(self):
        self.driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/tracking")

    def preprod(self):
        self.driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/tracking")

    def qa(self):
        self.driver.get ("https://funeral-director-frontend-qa.fnc-dev.co.uk/tracking")