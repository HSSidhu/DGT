from csv import excel
from datetime import datetime, timedelta
from idlelib.idle_test.test_idlehistory import line2

import arrow
from behave import *
from pip.cmdoptions import timeout
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from POM.AutomationDriver import AutomationDriver
from POM.BookingInPage import BookingInPage
from POM.FirstCallPage import FirstCallPage
from POM.LoginPage import LoginPage
from POM.MyUniqueID import MyUniqueID
from selenium.common.exceptions import NoSuchElementException

# @given("We have created First Call {Funeral_Home} {Deceased_FirstName} {Deceased_Lastname} {funeral_type} {url}")
# def step_impl(context, Funeral_Home: str, Deceased_FirstName : str, Deceased_Lastname : str, funeral_type : str, url : str):
#
#         driver = AutomationDriver.driver
#         base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next="
#         driver.get(base_url + "/")
#         driver.maximize_window()
#         driver.implicitly_wait(30)
#
#         #Today's Date
#         Todaysdate = arrow.now().format('DD/MM/YYYY')
#
#         login= LoginPage(driver)
#         login.UserName("harwinder.sidhu@coopdigital.co.uk")
#         login.Password("password")
#
#         #driver.find_element_by_id("djHideToolBarButton").click()
#
#         newfirstcall = FirstCallPage(driver)
#         newfirstcall.selectnewcall()
#         newfirstcall.setcallertitle("Mr")
#         newfirstcall.setcallerfirstname("Test")
#         newfirstcall.setcallerlastname("user")
#         newfirstcall.setcallermainphone("032132132133123")
#         newfirstcall.setcallerotherphone("03232131332324")
#         newfirstcall.setrelationship("Aunt")
#         newfirstcall.setmaincontact()
#         newfirstcall.setfuneralhome(Funeral_Home)
#         newfirstcall.setdeceasedtitle("Mr")
#         newfirstcall.setdeceasedfirstname(Deceased_FirstName)
#         newfirstcall.setdeceasedlastname(Deceased_Lastname)
#         newfirstcall.setdeceasedgendermale()
#         newfirstcall.setdeceasedreligion("Other")
#         newfirstcall.setdeceasedDOB("01/01/1944")
#         newfirstcall.setdeceasedDOD(Todaysdate)
#
#         if (funeral_type == "Burial"):
#             newfirstcall.setdeceasedCommitalburial()
#         else:
#             newfirstcall.setdeceasedCommitalcremation()
#
#         newfirstcall.setcoronerinvolvedyes()
#         newfirstcall.setdeathverifiedyes()
#         newfirstcall.setdeathregisteredyes()
#         newfirstcall.setdeceasedPOD("Manchester")
#         newfirstcall.setcollectionreq()
#         newfirstcall.setresidence()
#         newfirstcall.setcollectionsame()
#         newfirstcall.setappointmentnow()
#         newfirstcall.savefirstcall()
#         driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
#         driver.find_element_by_link_text("Log out").click()
#
#         print("First Call Created Successfully")
#
# @step("I have booked in the deceased in the Home {deceased_sitename} {Deceased_FirstName} {Deceased_Lastname} {Location_inHouse}{url}")
# def step_impl(context, deceased_sitename : str, Deceased_FirstName : str, Deceased_Lastname : str, Location_inHouse : str, url : str):
#
#     driver = AutomationDriver.driver
#     base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next="
#     driver.get(base_url + "/")
#     Dname = Deceased_FirstName+" "+Deceased_Lastname
#     #print(name)
#     login= LoginPage(driver)
#     login.UserName("harwinder.sidhu@coopdigital.co.uk")
#     login.Password("password")
#     #driver.find_element_by_id("djHideToolBarButton").click()
#
#     driver.implicitly_wait(30)
#     driver.find_element_by_link_text(Dname).click()
#     referenceid = AutomationDriver.driver.find_element_by_id("deceased-reference").text
#     UniqueID = referenceid.split(':')[1].strip()
#
#     #UniqueID = MyUniqueID.deceasedID(Deceased_FirstName+Deceased_Lastname)
#     # uniquefunction = MyUniqueID(Deceased_FirstName+Deceased_Lastname)
#     # UniqueID = uniquefunction.deceasedID(Deceased_FirstName+Deceased_Lastname)
#
#     # Booking Page #
#     driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/tracking/")
#     bookingin = BookingInPage(driver)
#     bookingin.locationName(deceased_sitename)
#     bookingin.checkin()
#
#     # Login Page #
#     login= LoginPage(driver)
#     login.UserName("edinburgh.fso@coopdigital.co.uk")
#     login.Password("password")
#
#     #driver.find_element_by_id("first_contact_id-204").click()
#     #driver.find_elements(By.CLASS_NAME("tap-link__inner__title"),'//[text() = "Benny Dore"]').click()
#     #driver.find_elements_by_class_name("tap-link__inner__title")
#     # #driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]/span')
#     # select_box = driver.find_elements_by_xpath(".//*[starts-with(@class,'tap-link__inner__title')]/span")
#     # options = [x for x in select_box.find_elements_by_tag_name("Benny Dore")] #this part is cool, because it searches the elements contained inside of select_box and then adds them to the list options if they have the tag name "options"
#     # for element in options:
#     # print (element.get_attribute("value"))
#     #for elem in driver.find_elements_by_xpath('.//span[@class = "icon icon-avatar"]'):
#     #print (elem.get_attribute("innerHTML"))
#
#     # Booking Page #
#     bookingin = BookingInPage(driver)
#     for elem in driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]'):
#         if elem.text == Dname:
#             ActionChains(driver).move_to_element(elem).click().perform()
#
#             bookingin.Wristband()
#             bookingin.DeceasedintoCare("Released by Family")
#             bookingin.AllChecksComplete()
#
#             driver.find_element_by_id("id_deceased_details-reference").send_keys(UniqueID)
#             driver.find_element_by_id("goto_booking_in_done").click()
#             driver.find_element_by_id("add-personal-effect").click()
#             driver.find_element_by_id("id_personal_effect_form-description").send_keys("testing")
#             driver.find_element_by_id("id_personal_effect_form-location").send_keys("testing")
#             driver.find_element_by_id("id_personal_effect_form-client_instruction_2").click()
#             driver.find_element_by_id("id_personal_effect_form-received_receipt_number").send_keys("312312")
#             driver.find_element_by_id("goto_personal_effects_list").click()
#             driver.find_element_by_id("goto_deceased_measurements").click()
#             driver.find_element_by_id("id_deceased_measurements-height").send_keys("12")
#             driver.find_element_by_id("id_deceased_measurements-width").send_keys("12")
#             driver.find_element_by_id("id_deceased_measurements-depth").send_keys("21")
#             driver.find_element_by_id("goto_deceased_location_assignment").click()
#
#             Select(driver.find_element_by_id("id_deceased_location_assignment-location_assignment")).select_by_visible_text("East Newington Place - Holding Area (10)")
#
#             driver.find_element_by_id("goto_deceased_notes").click()
#
#             driver.find_element_by_id("id_deceased_notes-deceased_booking_notes").send_keys("Notes for the user")
#             driver.find_element_by_id("goto_second_verification").click()
#
#             driver.find_element_by_id("id_second_verification-second_user_email").send_keys("edinburgh.fd@coopdigital.co.uk")
#             driver.find_element_by_id("id_second_verification-second_user_password").send_keys("password")
#             driver.find_element_by_id("goto_booking_in_done").click()
#             driver.find_element_by_id("id_second_deceased_details-completed_all_checks").click()
#             driver.find_element_by_id("id_second_deceased_details-reference").send_keys(UniqueID)
#             driver.find_element_by_id("goto_booking_in_done").click()
#             driver.find_element_by_id("goto_welcome_screen").click()
#             print("Deceased Booked in Successfully")
#         else:
#             print("Deceased Not available for Booking")
#         break
#
# @step("I have completed the Mortuary Flow {Deceased_FirstName} {Deceased_Lastname} {url}")
# def step_impl(context, Deceased_FirstName : str, Deceased_Lastname : str, url : str):
#
#     driver = AutomationDriver.driver
#     base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next="
#     driver.get(base_url + "/")
#     Dname = Deceased_FirstName+" "+Deceased_Lastname
#     login= LoginPage(driver)
#     login.UserName("harwinder.sidhu@coopdigital.co.uk")
#     login.Password("password")
#     #driver.find_element_by_id("djHideToolBarButton").click()
#     # driver.find_element_by_id("create_funeral_first_call_207").click()
#     # for elem in driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]'):
#     # m = driver.find_element_by_link_text(Dname).find_element_by_xpath(".//*[starts-with(@id,'create_funeral_first_call')]")
#
#     a = 2
#     while a < 20:
#         b = str(a)
#         name = driver.find_element_by_xpath(".//*[@id='funeral_list']/div["+b+"]/div/div[1]/h2").text
#         if name == Dname :
#             driver.find_element_by_xpath(".//*[@id='funeral_list']/div["+b+"]/div/div[3]/a[1]").click()
#             break
#         else:
#             a = a+1
#     #driver.find_element_by_link_text(Dname).click()
#     # Preparation Tile
#
#     referenceid = AutomationDriver.driver.find_element_by_id("deceased-reference").text
#     UniqueID = referenceid.split(':')[1].strip()
#
#     driver.find_element_by_link_text("Preparation").click()
#     driver.find_element_by_id("id_pacemaker_or_radioactive_implant_1").click()
#     driver.find_element_by_id("id_infectious_1").click()
#     driver.find_element_by_id("id_gown_1").click()
#     driver.find_element_by_id("id_permission_for_fingerprints_1").click()
#     driver.find_element_by_id("id_permission_for_fingerprints_description").clear()
#     driver.find_element_by_id("id_permission_for_fingerprints_description").send_keys("testing")
#     driver.find_element_by_id("id_intent_to_embalm_1").click()
#     driver.find_element_by_id("id_permission_to_embalm_received_1").click()
#     driver.find_element_by_id("save-progress").click()
#
#     #Coffin Selection
#
#     driver.find_element_by_link_text("Coffin order").click()
#     driver.find_element_by_link_text("Standard coffin").click()
#     driver.find_element_by_css_selector("#sub_code_CO229111 > div.tile--image > img.tile--image_img").click()
#     driver.find_element_by_id("select2-id_interior_colour-container").click()
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys("White")
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
#     driver.find_element_by_id("select").click()
#     driver.find_element_by_id("save-progress").click()
#
#     #Mortuary Flow
#
#     driver.find_element_by_id("side_nav_dashboard").click()
#
#     driver.find_element_by_id("select2-id_current_mortuary-container").click()
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys("East")
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
#     driver.find_element_by_id("apply_site_change").click()
#
#     driver.find_element_by_link_text(Dname).click()
#     driver.find_element_by_id("id_deceased-coroners_disposal_certificate_issued").click()
#
#     driver.find_element_by_id("select2-id_coffin_requirement-coffin_size-container").click()
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys("165")
#     driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)
#
#     driver.find_element_by_id("save-progress").click()
#
#     driver.find_element_by_id("search-filter__search-box__search").send_keys(Dname)
#     driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
#     driver.find_element_by_link_text(Dname).click()
#
#     driver.find_element_by_id("id_deceased_status-is_embalming_complete").click()
#     driver.find_element_by_id("id_deceased_status-is_first_offices").click()
#     driver.find_element_by_id("id_deceased_status-is_silver_fingerprints_complete").click()
#     driver.find_element_by_id("id_deceased_status-is_quality_control_passed").click()
#     driver.find_element_by_id("save-progress").click()
#
#     driver.find_element_by_id("search-filter__search-box__search").send_keys(Dname)
#     driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
#     driver.find_element_by_link_text(Dname).click()
#
#     driver.find_element_by_id("id_deceased_status-is_name_plate_complete").click()
#     driver.find_element_by_id("id_deceased_status-is_coffin_furnished").click()
#
#     driver.find_element_by_id("id_username").send_keys("edinburgh.fso@coopdigital.co.uk")
#     driver.find_element_by_id("id_password").send_keys("password")
#     driver.find_element_by_id("id_all_checks_completed").click()
#     driver.find_element_by_id("id_second_deceased_details-reference").send_keys(UniqueID)
#     driver.find_element_by_id("trigger-second-verification").click()
#
#     driver.find_element_by_id("id_deceased_status-is_dressed_in_gown").click()
#     driver.find_element_by_id("id_deceased_status-is_deceased_laid_in_coffin").click()
#     driver.find_element_by_id("save-progress").click()
#
#     driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
#     driver.find_element_by_link_text("Log out").click()
#
#     print("Mortuary Flow Completed. Deceased ready for Burial")
#
#     pass
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)



@step("I have booked in the deceased in the Home {deceased_sitename} {Deceased_FirstName} {Deceased_Lastname} {Location_inHouse}")
def step_impl(context, deceased_sitename, Deceased_FirstName, Deceased_Lastname, Location_inHouse):
    """
    :type context: behave.runner.Context
    :type deceased_sitename: str
    :type Deceased_FirstName: str
    :type Deceased_Lastname: str
    :type Location_inHouse: str
    """
    pass


@given("We have created First Call {Funeral_Home} {Deceased_FirstName} {Deceased_Lastname} {funeral_type} {url}")
def step_impl(context, Funeral_Home, Deceased_FirstName, Deceased_Lastname, funeral_type, url):
    """
    :type context: behave.runner.Context
    :type Funeral_Home: str
    :type Deceased_FirstName: str
    :type Deceased_Lastname: str
    :type funeral_type: str
    :type url: str
    """
    pass


@step("I have completed the Mortuary Flow {Deceased_FirstName} {Deceased_Lastname} {url}")
def step_impl(context, Deceased_FirstName, Deceased_Lastname, url):
    """
    :type context: behave.runner.Context
    :type Deceased_FirstName: str
    :type Deceased_Lastname: str
    :type url: str
    """
    pass


@step("I create an event in the calendar {Deceased_FirstName} {Deceased_Lastname} {url} {event_type}")
def step_impl(context, Deceased_FirstName, Deceased_Lastname, url, event_type : str):

    driver = AutomationDriver.driver
    base_url = "http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next="
    driver.get(base_url + "/")
    Dname = Deceased_FirstName+" "+Deceased_Lastname
    login= LoginPage(driver)
    login.UserName("harwinder.sidhu@coopdigital.co.uk")
    login.Password("password")

    driver.find_element_by_xpath(".//*[@id='side_nav_calendar']").click()

    elem = driver.find_element_by_xpath(".//*[@id='calendar-wrapper']/div[2]/div/table/tbody/tr/td/div[2]/div/div[2]/table/tbody/tr[20]/td[2]")
    ActionChains(driver).move_to_element(elem).click().perform()

    driver.find_element_by_class_name("select2-selection__placeholder").click()

    # Increment todays date by 1 day
    Todaysdate = arrow.now().format('DD/MM/YYYY')
    date1 = datetime.strptime(Todaysdate, "%d/%m/%Y")
    date2 = date1 + timedelta(days=1)
    modified_date = datetime.strftime(date2, "%d/%m/%Y")
    #

    if event_type == "Funeral":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[2]").click()
    elif event_type == "Other":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[3]").click()
    elif event_type == "ClientAppointments":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[4]").click()
    elif event_type == "OtherActivity":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[5]").click()
    elif event_type == "DeceasedVist":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[6]").click()
    elif event_type == "AmbulanceDuty":
        driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[2]/div[2]/div[1]/div[1]/select/option[7]").click()

    driver.find_element_by_xpath(".//*[@id='event_popup']/div/div[1]/h2").click()
    driver.find_element_by_xpath(".//*[@id='create_event_next']").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath(".//*[@id='id_funeral_arrangement_booking-start_0']").clear()
    driver.find_element_by_xpath(".//*[@id='id_funeral_arrangement_booking-start_0']").send_keys(modified_date)
    driver.find_element_by_id("id_funeral_arrangement_booking-start_1").click()
    driver.find_element_by_id("id_funeral_arrangement_booking-start_1").clear()
    driver.find_element_by_id("id_funeral_arrangement_booking-start_1").send_keys("09:30")
    driver.find_element_by_id("id_funeral_arrangement_booking-end_1").clear()
    driver.find_element_by_id("id_funeral_arrangement_booking-end_1").send_keys("12:30")

    driver.find_element_by_id("select2-id_deceased_selection-deceased-container").click()
    driver.find_element_by_css_selector("input.select2-search__field").send_keys(Dname)
    driver.find_element_by_css_selector("input.select2-search__field").send_keys(Keys.RETURN)

    driver.find_element_by_id("select2-id_deceased_selection-deceased-container").click()
    driver.find_element_by_id("select2-id_funeral_arrangement-officiant-container").click()
    driver.find_element_by_id("select2-id_funeral_arrangement-place_of_service-container").click()

    driver.find_element_by_id("id_funeral_arrangement-burial_cremation_1").click()

    driver.find_element_by_css_selector("#id_funeral_arrangement-burial_cremation_0_anchor > label.tap-check.tap-check--inline").click()

    driver.find_element_by_id("id_funeral_arrangement-charity_one").send_keys("Charity 1")
    driver.find_element_by_id("id_funeral_arrangement-charity_two").send_keys("Charity 2")
    driver.find_element_by_id("id_funeral_arrangement-event_notes").send_keys("Ceremony Notes to be typed here")
    driver.find_element_by_id("save-progress").click()

    # if (!driver.findElements(By.Id("some_ID")).isEmpty && driver.findElements(By.Id("some_ID")).get(0).isDispalyed() ) {
    # = element Exists AND is visible

    # if (driver.find_element_by_xpath(".//*[@id='form-errors']/ul))

    # def IsTestElementPresent(driver)
    #     try:
    #         driver.find_element_by_xpath(".//*[@id='form-errors']/ul")
    #     return True
    #     If True
    #
    #         i=1
    #         while i < 8:
    #             elem = driver.find_element_by_xpath(".//*[@id='form-errors']/ul").text
    #             if elem == "Funeral director "+ "Harwinder Sidhu"+" not available. Please select another time.":
    #                 driver.find_element_by_id("select2-id_deceased_selection-deceased-container").click()
    #                 driver.find_element_by_id("select2-id_funeral_arrangement-officiant-container").click()
    #                 driver.find_element_by_id("select2-id_funeral_arrangement-place_of_service-container").click()
    #                 #driver.find_element_by_id("save-progress").click()
    #         i = i + 1

