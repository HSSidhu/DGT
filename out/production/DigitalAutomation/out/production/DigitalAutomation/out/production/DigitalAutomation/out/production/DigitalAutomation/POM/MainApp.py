import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MainApp(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def local(self):
        self.driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next=/")

    def preprod(self):
        self.driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/credentials/login/?next=/")

    def qa(self):
        self.driver.get ("https://funeral-director-frontend-qa.fnc-dev.co.uk/credentials/login/?next=/")