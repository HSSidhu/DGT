from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class NewUserPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def UserRole(self, role):
        self.driver.find_element_by_id("select2-id_user-role-container").click()
        for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
            if elem.text == role:
                ActionChains(self.driver).move_to_element(elem).click().perform()
                break

    # def FuneralServiceOperator(self, fso):
    #     self.driver.find_element_by_id("select2-id_user-role-container").click()
    #     for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
    #         if elem.text == fso:
    #             ActionChains(self.driver).move_to_element(elem).click().perform()
    #
    # def LogisticsManager(self, lm):
    #     self.driver.find_element_by_id("select2-id_user-role-container").click()
    #     for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
    #         if elem.text == lm:
    #             ActionChains(self.driver).move_to_element(elem).click().perform()
    #
    # def RegionalManager(self, rm):
    #     self.driver.find_element_by_id("select2-id_user-role-container").click()
    #     for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
    #         if elem.text == rm:
    #             ActionChains(self.driver).move_to_element(elem).click().perform()
    #
    # def MortuaryStaff(self, Mortuary):
    #     self.driver.find_element_by_id("select2-id_user-role-container").click()
    #     for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
    #         if elem.text == Mortuary:
    #             ActionChains(self.driver).move_to_element(elem).click().perform()
    #
    # def ColleagueID(self, Id):
    #     self.driver.find_element_by_id("id_staff_member-staff_id_number").send_keys(Id)

    #################PRIMARY SITE############################################

    def sitelocation(self, sitename):
        self.driver.find_element_by_id("select2-id_staff_member-primary_site-container").click()
        for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_staff_member-primary_site-results']/li"):
            if elem.text == sitename:
                ActionChains(self.driver).move_to_element(elem).click().perform()
                break

    #################SECONDARY SITE############################################

    def SecondarySite(self, secondarysite):
        self.driver.find_element_by_id("id_staff_member-secondary_sites_anchor").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(secondarysite)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def ContractedHours(self, hours):
        self.driver.find_element_by_id("id_staff_member-contracted_hours_per_week").send_keys(hours)

    def Savedetails(self):
        self. driver.find_element_by_id("save-progress").click()

    def StaffNumber(self):
        self. driver.find_element_by_id("save-progress").click()

