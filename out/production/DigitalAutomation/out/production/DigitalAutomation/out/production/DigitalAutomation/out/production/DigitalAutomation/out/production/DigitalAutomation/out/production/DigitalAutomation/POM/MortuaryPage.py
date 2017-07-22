from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from POM import FirstCallPage
from POM.CalendarPage import CalendarPage


class MortuaryPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

                            ## PREPATAION Tile##
    def PreparationTile(self):
        self.driver.find_element_by_link_text("Preparation").click()
    def Pacemaker(self):
        self.driver.find_element_by_id("id_pacemaker_or_radioactive_implant_1").click()
    def Infectious(self):
        self.driver.find_element_by_id("id_infectious_1").click()
    def Gown(self):
        self.driver.find_element_by_id("id_gown_1").click()
    def FingerPrints(self):
        self.driver.find_element_by_id("id_permission_for_fingerprints_1").click()
    def FingerPrintPermission(self, permission):
        self.driver.find_element_by_id("id_permission_for_fingerprints_description").clear()
        self.driver.find_element_by_id("id_permission_for_fingerprints_description").send_keys(permission)
    def Embalm(self):
        self.driver.find_element_by_id("id_intent_to_embalm_1").click()  # Embalming is YES
    def EmbalmPermission(self):
        self.driver.find_element_by_id("id_permission_to_embalm_received_1").click() # Permission is YES
    def SavePreparation(self):
        self.driver.find_element_by_id("save-progress").click()

        ## Coffin Selection Tile##

    def CoffinTile(self):
        self.driver.find_element_by_link_text("Coffin order").click()
    def StandardCoffin(self):
        self.driver.find_element_by_link_text("Standard coffin").click()
    def SelectCoffinImage(self):
        self.driver.find_element_by_css_selector("#sub_code_CO229111 > div.tile--image > img.tile--image_img").click()
    def CoffinColour(self, colour):
        self. driver.find_element_by_id("select2-id_interior_colour-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(colour)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
    def SelectCoffin(self):
        self. driver.find_element_by_id("select").click()
    def SaveCoffin(self):
        self.driver.find_element_by_id("save-progress").click()

        ## Mortuary Flow ##

    def MenuBar(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//div[@id='top-navigation']/header/div/div/button").click()

    def CareAndPrep(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("side_nav_dashboard").click()

    def SelectMortuary(self, Mortuary):
        self.driver.find_element_by_id("select2-id_current_mortuary-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Mortuary)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
        self.driver.find_element_by_id("apply_site_change").click()

    def FindDeceased(self, Dname):
        self.driver.find_element_by_link_text(Dname).click()

    def CareandPrepForm(self, coffinsize):
        self.driver.find_element_by_id("id_deceased-coroners_disposal_certificate_issued").click()
        self.driver.find_element_by_id("select2-id_coffin_requirement-coffin_size-container").click()
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(coffinsize)
        self.driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
        self.driver.find_element_by_id("save-progress").click()

    def SearchDeceased(self, Dname):
        self.driver.find_element_by_id("search-filter__search-box__search").send_keys(Dname)
        self.driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        self.driver.find_element_by_link_text(Dname).click()

    def DressingandCoffin(self):
        self.driver.find_element_by_id("id_deceased_status-is_embalming_complete").click()
        self.driver.find_element_by_id("id_deceased_status-is_first_offices").click()
        self.driver.find_element_by_id("id_deceased_status-is_silver_fingerprints_complete").click()
        self.driver.find_element_by_id("id_deceased_status-is_quality_control_passed").click()
        self.driver.find_element_by_id("id_deceased_status-is_care_and_preparation_complete").click()
        self.driver.find_element_by_id("save-progress").click()

    def Encoffin(self, UniqueID, SecondVerficatioEmail, SecondVerficatioPass):
        self.driver.find_element_by_id("id_deceased_status-is_name_plate_complete").click()
        self.driver.find_element_by_id("id_deceased_status-is_coffin_finished").click()
        self.driver.find_element_by_id("id_deceased_status-is_coffin_furnished").click()
        self.driver.find_element_by_id("id_username").send_keys(SecondVerficatioEmail)
        self.driver.find_element_by_id("id_password").send_keys(SecondVerficatioPass)
        self.driver.find_element_by_id("id_all_checks_completed").click()
        self.driver.find_element_by_id("id_second_deceased_details-reference").send_keys(UniqueID)
        self.driver.find_element_by_id("trigger-second-verification").click()
        self.driver.find_element_by_id("id_deceased_status-is_dressed_in_gown").click()
        self.driver.find_element_by_id("id_deceased_status-is_deceased_laid_in_coffin").click()
        self.driver.find_element_by_id("save-progress").click()

    def Logout(self):
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()


