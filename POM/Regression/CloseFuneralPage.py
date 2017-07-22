from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class FirstCallPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def selectnewcall(self):
        self.driver.find_element_by_id("new_call").click()