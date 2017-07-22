from POM.Helpers.AutomationDriver import AutomationDriver


class MyUniqueID(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def deceasedID(self, deceasedname):
        self.driver.find_element_by_link_text(deceasedname).click()
        referenceid = AutomationDriver.driver.find_element_by_id("deceased-reference").text
        unique = referenceid.split(':')[1].strip()
        return unique

    def AfterArrangementID(self):
        referenceid = AutomationDriver.driver.find_element_by_id("deceased-reference").text
        unique = referenceid.split(':')[1].strip()
        return unique
