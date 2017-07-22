from selenium.webdriver.common.keys import Keys


class FirstCallPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def selectnewcall(self):
        self.driver.find_element_by_id("new_call").click()

    def FirstCallGeneraldetails(self, callertitle, callerfirstname, callerlastname, callermainphone, callerotherphone,callerrelation, funeralhome):

        self.driver.find_element_by_id("select2-id_first_contact-client_title-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(callertitle)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

        self.driver.find_element_by_id("id_first_contact-client_first_name").clear()
        self.driver.find_element_by_id("id_first_contact-client_first_name").send_keys(callerfirstname)
        self.driver.find_element_by_id("id_first_contact-client_last_name").clear()
        self.driver.find_element_by_id("id_first_contact-client_last_name").send_keys(callerlastname)
        self.driver.find_element_by_id("id_first_contact-client_telephone_number").clear()
        self.driver.find_element_by_id("id_first_contact-client_telephone_number").send_keys(callermainphone)
        self.driver.find_element_by_id("id_first_contact-client_mobile_telephone_number").clear()
        self.driver.find_element_by_id("id_first_contact-client_mobile_telephone_number").send_keys(callerotherphone)

        self.driver.find_element_by_id("select2-id_first_contact-client_relationship-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(callerrelation)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

        self.driver.find_element_by_id("id_first_contact-client_main_contact_1").click()

        self.driver.find_element_by_id("select2-id_first_contact-funeral_home-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(funeralhome)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)


    def FirstCallDeceasedDetails(self, deceasedtitle, deceasedfirstname, deceasedlastname, deceasedreligion, deceasedDOB, deceasedDOD, deceasedPOD):

        self.driver.find_element_by_id("select2-id_deceased-title-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(deceasedtitle)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

        self.driver.find_element_by_id("id_deceased-first_name").clear()
        self.driver.find_element_by_id("id_deceased-first_name").send_keys(deceasedfirstname)
        self.driver.find_element_by_id("id_deceased-last_name").clear()
        self.driver.find_element_by_id("id_deceased-last_name").send_keys(deceasedlastname)
        self.driver.find_element_by_id("id_deceased-gender_1").click()

        self.driver.find_element_by_id("select2-id_deceased-religion-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(deceasedreligion)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

        self.driver.find_element_by_id("id_deceased-date_of_birth").clear()
        self.driver.find_element_by_id("id_deceased-date_of_birth").send_keys(deceasedDOB)

        self.driver.find_element_by_id("id_deceased-date_of_death").clear()
        self.driver.find_element_by_id("id_deceased-date_of_death").send_keys(deceasedDOD)

        self.driver.find_element_by_id("id_first_contact-burial_cremation_1").click()   # set deceased Commital burial
        #self.driver.find_element_by_id("id_first_contact-burial_cremation_2").click()  # setd eceased Commital cremation
        self.driver.find_element_by_id("id_deceased-coroner_involved_1").click()        # set coronerinvolved yes
        self.driver.find_element_by_id("id_deceased-verification_of_death_1").click()   # set death verified yes
        self.driver.find_element_by_id("id_deceased-registration_of_death_1").click()   # set death registered yes
        self.driver.find_element_by_id("id_first_contact-place_of_death_address_line_one").clear()
        self.driver.find_element_by_id("id_first_contact-place_of_death_address_line_one").send_keys(deceasedPOD)

    def FirstCallDeceasedOtherDetails(self):
        self.driver.find_element_by_id("id_first_contact-book_collection_now_1").click()
        self.driver.find_element_by_css_selector("#id_first_contact-book_collection_now_0_anchor > label.tap-check.tap-check--inline").click()

        self.driver.find_element_by_id("id_first_contact-collection_type_of_residence_1").click()
        self.driver.find_element_by_css_selector("#id_first_contact-collection_type_of_residence_0_anchor > label.tap-check.tap-check--inline").click()

        self.driver.find_element_by_id("id_first_contact-collection_same_as_place_of_death").click()
        #self.driver.find_element_by_css_selector("#id_first_contact-collection_same_as_place_of_death_anchor > label.tap-check").click()

        self.driver.find_element_by_id("id_first_contact-appointment_book_1").click()

    def savefirstcall(self):
        self.driver.find_element_by_css_selector("button.btn-primary.btn-save-first-contact").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()

# FIRST CALL SAVED #


