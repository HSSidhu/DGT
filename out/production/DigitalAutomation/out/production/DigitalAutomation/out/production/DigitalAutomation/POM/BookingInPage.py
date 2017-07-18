import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class BookingInPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def locationName(self, SelectLocation):
        self.driver.find_element_by_id("select2-id_sites-container").click()
        self.driver.find_element_by_class_name("select2-search__field").send_keys(SelectLocation)
        self.driver.find_element_by_class_name("select2-search__field").send_keys(Keys.RETURN)
        self.driver.find_element_by_id("submit-site").click()

    def checkin(self):
        self.driver.find_element_by_xpath("//a[@id='checkin']/div").click()

    def Wristband(self):
        self.driver.find_element_by_id("id_deceased_details-has_non_fnc_wristband_0").click()

    def DeceasedintoCare(self, sendintocare):
        self.driver.find_element_by_id("id_deceased_details-released_into_our_care_by").send_keys(sendintocare)

    def AllChecksComplete(self):
        self.driver.find_element_by_id("id_deceased_details-completed_all_checks").click()


