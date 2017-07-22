import objects as objects
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from POM.CalendarPage import CalendarPage
from POM.MyUniqueID import MyUniqueID


class BookingOutPage(object):

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

    def checkout(self):
        self.driver.find_element_by_xpath(".//*[@id='checkout']/div").click()

    def AllChecksComplete(self, UniqueID):
        self.driver.find_element_by_id("id_deceased_details-completed_all_checks").click()
        self.driver.find_element_by_id("id_deceased_details-reference").send_keys(UniqueID)
        self.driver.find_element_by_xpath(".//*[@id='goto_booking_out_done']").click()
        self.driver.find_element_by_xpath(".//*[@id='id_deceased_notes-deceased_booking_notes']").send_keys("Notes for the user while Booking OUT \n ")
        self.driver.find_element_by_id("goto_day_of_committal").click()
        self.driver.find_element_by_id("id_day_of_committal-final_checks_0").click()
        self.driver.find_element_by_id("goto_booking_out_next").click()


    def PerformFinalChecks(self):

        self.driver.find_element_by_id("id_coffin_details-coffin_checked").click() # Coffin details
        self.driver.find_element_by_id("goto_booking_out_flowers").click()

        self.driver.find_element_by_id("id_flower_details-flowers_checked").click() # Flower Details
        self.driver.find_element_by_id("goto_booking_out_done").click()

        self.driver.find_element_by_id("id_stationery_details-stationery_checked").click() # Stationary Details
        self.driver.find_element_by_id("goto_booking_out_flowers").click()

        self.driver.find_element_by_id("id_notes-notes_checked").click() # Notes Check
        self.driver.find_element_by_id("goto_booking_out_flowers").click()

        self.driver.find_element_by_id("id_final_checks-read_about_me").click()
        self.driver.find_element_by_id("id_final_checks-briefed_and_understood").click()
        self.driver.find_element_by_id("id_final_checks-pause_for_thought_colleagues").send_keys("John Graves\n", "Ben Roger")
        self.driver.find_element_by_id("id_final_checks-notes").send_keys("No Issues in the Process")
        self.driver.find_element_by_id("goto_booking_out_done").click()

    def SecondValidation(self, email, password, UniqueID):
        self.driver.find_element_by_id("id_second_verification-second_user_email").send_keys(email)
        self.driver.find_element_by_id("id_second_verification-second_user_password").send_keys(password)
        self.driver.find_element_by_id("goto_booking_out_next").click()
        self.driver.find_element_by_id("id_second_deceased_details-completed_all_checks").click()
        self.driver.find_element_by_id("id_second_deceased_details-completed_final_checks").click()
        self.driver.find_element_by_id("id_second_deceased_details-reference").send_keys(UniqueID)
        self.driver.find_element_by_id("goto_booking_out_done").click()
        self.driver.find_element_by_id("goto_welcome_screen").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()
