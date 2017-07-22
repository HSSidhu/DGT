from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from POM.Regression.CalendarPage import CalendarPage


class BookingInPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def NavBar(self):
        CalendarPage.NavBar()

    def TrackingApp(self):
        self.driver.find_element_by_id("side_nav_open_tracking_app").click()

    def FindDeceased(self, dname):
        self.driver.find_element_by_link_text(dname).click()

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

    def BookIn(self,UniqueID ):
        self.driver.find_element_by_id("id_deceased_details-reference").send_keys(UniqueID)
        self.driver.find_element_by_id("goto_booking_in_done").click()
        self.driver.find_element_by_id("add-personal-effect").click()
        self.driver.find_element_by_id("id_personal_effect_form-description").send_keys("testing")
        self.driver.find_element_by_id("id_personal_effect_form-location").send_keys("testing")
        self.driver.find_element_by_id("id_personal_effect_form-client_instruction_2").click()
        self.driver.find_element_by_id("id_personal_effect_form-received_receipt_number").send_keys("312312")
        self.driver.find_element_by_id("goto_personal_effects_list").click()
        self.driver.find_element_by_id("goto_deceased_measurements").click()
        self.driver.find_element_by_id("id_deceased_measurements-height").send_keys("12")
        self.driver.find_element_by_id("id_deceased_measurements-width").send_keys("12")
        self.driver.find_element_by_id("id_deceased_measurements-depth").send_keys("21")
        self.driver.find_element_by_id("goto_deceased_location_assignment").click()

    def Location(self): # will always pick second option of any Funeral Home
        Select(self.driver.find_element_by_id("id_deceased_location_assignment-location_assignment")).select_by_index(2)
        self.driver.find_element_by_id("goto_deceased_notes").click()
        self.driver.find_element_by_id("id_deceased_notes-deceased_booking_notes").send_keys("Notes for the user while Booking In \n")
        self.driver.find_element_by_id("goto_second_verification").click()

    def SecondValidation(self, email, password, UniqueID):
        self.driver.find_element_by_id("id_second_verification-second_user_email").send_keys(email)
        self.driver.find_element_by_id("id_second_verification-second_user_password").send_keys(password)
        self.driver.find_element_by_id("goto_booking_in_done").click()
        self.driver.find_element_by_id("id_second_deceased_details-completed_all_checks").click()
        self.driver.find_element_by_id("id_second_deceased_details-reference").send_keys(UniqueID)
        self.driver.find_element_by_id("goto_booking_in_done").click()
        self.driver.find_element_by_id("goto_welcome_screen").click()


