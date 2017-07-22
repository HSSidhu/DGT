from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class DjangoPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def EnterUserDetails(self, email1, password1, num1, num2, location):
        self.driver.find_element_by_xpath(".//*[@id='content-main']/ul/li/a").click()  # Add User
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys(email1)
        self.driver.find_element_by_id("id_password1").send_keys(password1)
        self.driver.find_element_by_id("id_password2").send_keys(password1)
        self.driver.find_element_by_id("id_staffmember-0-uuid").send_keys(num1)
        self.driver.find_element_by_id("id_staffmember-0-staff_id_number").send_keys(num2)
        self.driver.find_element_by_id("id_staffmember-0-primary_site").click()
        if location == "Edinburgh":
            Select(self.driver.find_element_by_id("id_staffmember-0-primary_site")).select_by_visible_text("East Newington Place")
            self.driver.find_element_by_xpath(".//*[@id='id_staffmember-0-secondary_sites']/option[20]").click() # Colinton
        else:
            Select(self.driver.find_element_by_id("id_staffmember-0-primary_site")).select_by_visible_text("Arden House")
            self.driver.find_element_by_xpath(".//*[@id='id_staffmember-0-secondary_sites']/option[9]").click() # Bolton

        self.driver.find_element_by_xpath(".//*[@id='id_staffmember-0-capabilities']/option[8]").click()
        self.driver.find_element_by_id("id_staffmember-0-contracted_hours_per_week").send_keys("37.5")
        self.driver.find_element_by_name("_continue").click()

    def ReEnterDetails(self, username1, lastname1, email1):
        self.driver.find_element_by_id("id_first_name").clear()
        self.driver.find_element_by_id("id_first_name").send_keys(username1)
        self.driver.find_element_by_id("id_last_name").clear()
        self.driver.find_element_by_id("id_last_name").send_keys(lastname1)
        self.driver.find_element_by_id("id_email").clear()
        self.driver.find_element_by_id("id_email").send_keys(email1)
        self.driver.find_element_by_xpath(".//*[@id='id_groups']/option[4]").click()
        self.driver.find_element_by_name("_save").click()

    def Logout(self):
        elem = self.driver.find_element_by_xpath(".//*[@id='header']/div[2]/a[3]")
        ActionChains(self.driver).move_to_element(elem).click().perform()
