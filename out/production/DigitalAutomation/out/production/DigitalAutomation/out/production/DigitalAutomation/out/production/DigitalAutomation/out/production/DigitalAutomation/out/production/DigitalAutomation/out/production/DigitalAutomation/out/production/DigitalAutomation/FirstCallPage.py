from selenium.webdriver.common.keys import Keys

from POM.CalendarPage import CalendarPage


class FirstCallPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def selectnewcall(self):
        self.driver.find_element_by_id("new_call").click()

    def setcallertitle(self, callertitle):
        self.driver.find_element_by_id("select2-id_first_contact-client_title-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(callertitle)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def setcallerfirstname(self, callerfirstname):
        self.driver.find_element_by_id("id_first_contact-client_first_name").clear()
        self.driver.find_element_by_id("id_first_contact-client_first_name").send_keys(callerfirstname)

    def setcallerlastname(self, callerlastname):
        self.driver.find_element_by_id("id_first_contact-client_last_name").clear()
        self.driver.find_element_by_id("id_first_contact-client_last_name").send_keys(callerlastname)

    def setcallermainphone(self, callermainphone):
        self.driver.find_element_by_id("id_first_contact-client_telephone_number").clear()
        self.driver.find_element_by_id("id_first_contact-client_telephone_number").send_keys(callermainphone)

    def setcallerotherphone(self, callerotherphone):
        self.driver.find_element_by_id("id_first_contact-client_mobile_telephone_number").clear()

        self.driver.find_element_by_id("id_first_contact-client_mobile_telephone_number").send_keys(callerotherphone)

    def setrelationship(self, callerrelation):
        self.driver.find_element_by_id("select2-id_first_contact-client_relationship-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(callerrelation)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def setmaincontact(self):
        self.driver.find_element_by_id("id_first_contact-client_main_contact_1").click()

    def setfuneralhome(self, funeralhome):
        self.driver.find_element_by_id("select2-id_first_contact-funeral_home-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(funeralhome)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def setdeceasedtitle(self, deceasedtitle):
        self.driver.find_element_by_id("select2-id_deceased-title-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(deceasedtitle)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def setdeceasedfirstname(self, deceasedfirstname):
        self.driver.find_element_by_id("id_deceased-first_name").clear()
        self.driver.find_element_by_id("id_deceased-first_name").send_keys(deceasedfirstname)

    def setdeceasedlastname(self, deceasedlastname):
        self.driver.find_element_by_id("id_deceased-last_name").clear()
        self.driver.find_element_by_id("id_deceased-last_name").send_keys(deceasedlastname)

    def setdeceasedgendermale(self):
        self.driver.find_element_by_id("id_deceased-gender_1").click()

    def setdeceasedreligion(self, deceasedreligion):
        self.driver.find_element_by_id("select2-id_deceased-religion-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(deceasedreligion)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def setdeceasedDOB(self, deceasedDOB):
        self.driver.find_element_by_id("id_deceased-date_of_birth").clear()
        self.driver.find_element_by_id("id_deceased-date_of_birth").send_keys(deceasedDOB)

    def setdeceasedDOD(self, deceasedDOD):
        self.driver.find_element_by_id("id_deceased-date_of_death").clear()
        self.driver.find_element_by_id("id_deceased-date_of_death").send_keys(deceasedDOD)

    def setdeceasedCommitalburial(self):
        self.driver.find_element_by_id("id_first_contact-burial_cremation_1").click()

    def setdeceasedCommitalcremation(self):
        self.driver.find_element_by_id("id_first_contact-burial_cremation_2").click()

    def setcoronerinvolvedyes(self):
        self.driver.find_element_by_id("id_deceased-coroner_involved_1").click()

    def setdeathverifiedyes(self):
        self.driver.find_element_by_id("id_deceased-verification_of_death_1").click()

    def setdeathregisteredyes(self):
        self.driver.find_element_by_id("id_deceased-registration_of_death_1").click()

    def setdeceasedPOD(self, deceasedPOD):
        self.driver.find_element_by_id("id_first_contact-place_of_death_address_line_one").clear()
        self.driver.find_element_by_id("id_first_contact-place_of_death_address_line_one").send_keys(deceasedPOD)

    def setcollectionreq(self):
        self.driver.find_element_by_id("id_first_contact-book_collection_now_1").click()
        self.driver.find_element_by_css_selector("#id_first_contact-book_collection_now_0_anchor > label.tap-check.tap-check--inline").click()

    def setresidence(self):
        self.driver.find_element_by_id("id_first_contact-collection_type_of_residence_1").click()
        self.driver.find_element_by_css_selector("#id_first_contact-collection_type_of_residence_0_anchor > label.tap-check.tap-check--inline").click()

    def setcollectionsame(self):
        self.driver.find_element_by_id("id_first_contact-collection_same_as_place_of_death").click()
        #self.driver.find_element_by_css_selector("#id_first_contact-collection_same_as_place_of_death_anchor > label.tap-check").click()

    def setappointmentnow(self):
        self.driver.find_element_by_id("id_first_contact-appointment_book_1").click()

    def savefirstcall(self):
        self.driver.find_element_by_css_selector("button.btn-primary.btn-save-first-contact").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()

# FIRST CALL SAVED #


