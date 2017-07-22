from selenium.webdriver.common.keys import Keys

class CalendarPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def NavBar(self):
        self.driver.find_element_by_xpath("//div[@id='top-navigation']/header/div/div/button").click()

    def CalendarEvent(self):
        self.driver.find_element_by_xpath(".//*[@id='side_nav_calendar']").click()

    def NewEvent(self):
        self.driver.find_element_by_id("new_event_picker_button").click()

    def FuneralBooking(self):
        self.driver.find_element_by_id("new_event_type_create_funeral_booking").click()

    def StaffBooking(self):
        self.driver.find_element_by_id("new_event_type_create_staff_booking").click()

    def ClientBooking(self):
        self.driver.find_element_by_id("new_event_type_create_client_appointment_option").click()

    def CeremonialEvents(self):
        self.driver.find_element_by_id("new_event_type_create_ceremonial_event").click()

    def DeceasedVisit(self):
        self.driver.find_element_by_id("new_event_type_create_deceased_visit_option").click()

    def AmbulanceDuty(self):
        self.driver.find_element_by_id("new_event_type_create_ambulance_duty_option").click()

    def SelectCategory(self):
        self.driver.find_element_by_id("new_event_dialog-picker-ok").click()

    def BookingStartDate(self, BookingStartDate):
        self.driver.find_element_by_xpath(".//*[@id='id_funeral_arrangement_booking-start_0']").clear()
        self.driver.find_element_by_xpath(".//*[@id='id_funeral_arrangement_booking-start_0']").send_keys(BookingStartDate)

    def BookingStartTime(self, BookingStartTime):
        self.driver.find_element_by_id("id_funeral_arrangement_booking-start_1").clear()
        self.driver.find_element_by_id("id_funeral_arrangement_booking-start_1").click()
        self.driver.find_element_by_id("id_funeral_arrangement_booking-start_1").send_keys(BookingStartTime)

    def BookingEndTime(self, BookingEndTime):
        self.driver.find_element_by_id("id_funeral_arrangement_booking-end_1").clear()
        self.driver.find_element_by_id("id_funeral_arrangement_booking-end_1").send_keys(BookingEndTime)

    def DeceasedName(self, DeceasedName):
        self.driver.find_element_by_id("select2-id_deceased_selection-deceased-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(DeceasedName)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    def Burial(self):
        self.driver.find_element_by_id("id_funeral_arrangement-burial_cremation_1").click()

    def Charity1(self, Charity1):
        self.driver.find_element_by_id("id_funeral_arrangement-charity_one").send_keys(Charity1)

    def Charity2(self, Charity2):
        self.driver.find_element_by_id("id_funeral_arrangement-charity_two").send_keys(Charity2)

    def Notes(self, Notes):
        self.driver.find_element_by_id("id_funeral_arrangement-event_notes").send_keys(Notes)

    def SaveEvent(self):
        self.driver.find_element_by_id("save-progress").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()






