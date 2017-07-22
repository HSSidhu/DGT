from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class NewUserPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    #################User ROLE###############################################
    def UserRole(self, role):
        self.driver.find_element_by_id("select2-id_user-role-container").click()
        for elem in self.driver.find_elements_by_xpath(".//*[@id='select2-id_user-role-results']/li"):
            if elem.text == role:
                ActionChains(self.driver).move_to_element(elem).click().perform()
                break

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

    ###########################################################################
    def ContractedHours(self, hours):
        self.driver.find_element_by_id("id_staff_member-contracted_hours_per_week").send_keys(hours)

        ####################CAPABILITIES##################################

        # 1		can_drive_hearse
        # 2		can_drive_limo
        # 3		can_bear_coffin
        # 4		can_embalm_deceased
        # 5		can_drive_ambulance
        # 6		can_arrange_funeral
        # 7		can_conduct_funeral
        # 8		can_administer_users
        # 9		can_administer_budgets
        # 10	can_view_security_audit
        # 11	can_schedule_resources
        # 12	can_administer_scheduler_settings

    def FindUser(self, email):
        self.driver.find_element_by_link_text(email).click()

    def FDCapabilities(self):
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[8]").click()
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[11]").click()
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[12]").click()

    def FSOcapabilities(self):
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()

    def RMCapabilities(self):
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()

    def MortuaryCapabilities(self):
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()

    def LMCapabilities(self):
        self.driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()

    def SaveNewUserDetails(self):
        self.driver.find_element_by_id("save-progress").click()

    def OpenMenuLink(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//div[@id='top-navigation']/header/div/div/button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("side_nav_staff_admin_list_view").click()

    def AddUserLink(self, email, username2, lastname2, num1, colleagueid):
        self.driver.find_element_by_id("add_user").click()
        self.driver.find_element_by_id("id_user-email").send_keys(email)
        self.driver.find_element_by_id("id_user-first_name").send_keys(username2)
        self.driver.find_element_by_id("id_user-last_name").send_keys(lastname2)
        self.driver.find_element_by_id("id_staff_member-primary_mobile_number").send_keys(num1)
        self.driver.find_element_by_id("id_staff_member-staff_id_number").send_keys(colleagueid)

    def ResetPassword(self, email, name, password):
        self.driver.find_element_by_id("searchbar").clear()
        self.driver.find_element_by_id("searchbar").send_keys(email)
        self.driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.driver.find_element_by_link_text(name).click()
        self.driver.find_element_by_link_text("this form").click()

        self.driver.find_element_by_id("id_password1").send_keys(password)
        self.driver.find_element_by_id("id_password2").send_keys(password)

        self.driver.find_element_by_css_selector("input.default").click()
        self.driver.find_element_by_name("_save").click()
