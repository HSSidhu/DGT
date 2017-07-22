from datetime import datetime, timedelta

import arrow
from behave import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

from POM.Helpers.AutomationDriver import AutomationDriver
from POM.Helpers.MainApp import MainApp
from POM.Helpers.TrackingApp import TrackingApp
from POM.Regression.BookingInPage import BookingInPage
from POM.Regression.BookingOutPage import BookingOutPage
from POM.Regression.CalendarPage import CalendarPage
from POM.Regression.FirstCallPage import FirstCallPage
from POM.Regression.MortuaryPage import MortuaryPage
from POM.Regression.MyUniqueID import MyUniqueID
from POM.TestData.DataSheetPage import DataSheetPage


@given(
    "We have created First Call {Funeral_Home} {Deceased_FirstName} {Deceased_Lastname} {funeral_type} {Environment} {hub}")
def step_impl(context, Funeral_Home, Deceased_FirstName, Deceased_Lastname, funeral_type, Environment, hub):

        driver = AutomationDriver.driver
        driver.maximize_window()

        mainapp = MainApp(driver)

        if Environment == "local":
            mainapp.local()
        elif Environment =="preprod" :
            mainapp.preprod()
        elif Environment == "qa":
            mainapp.qa()

        driver.implicitly_wait(30)
        Todaysdate = arrow.now().format('DD/MM/YYYY')

        RegresstionTestUsers = DataSheetPage(driver)  # Detail for the Login Users @excel
        RegresstionTestUsers.LoginUsers(hub)          # Detail for the Login Users @excel

        newfirstcall = FirstCallPage(driver)
        newfirstcall.selectnewcall()
        newfirstcall.FirstCallGeneraldetails("Mr", "Test", "User", "01234567897", "010234654327869","Aunt", Funeral_Home)
        newfirstcall.FirstCallDeceasedDetails("Mr", Deceased_FirstName, Deceased_Lastname, "Other", "01/01/1944", Todaysdate, "Manchester")
        newfirstcall.FirstCallDeceasedOtherDetails()
        newfirstcall.savefirstcall()   # Includes TRY and CATCH check
        newfirstcall.Logout()

@step("I have booked IN the deceased {Environment} {deceased_sitename} {Deceased_FirstName} {Deceased_Lastname} {hub}")
def step_impl(context, Environment, deceased_sitename, Deceased_FirstName, Deceased_Lastname, hub):

    driver = AutomationDriver.driver

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod":
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    Dname = Deceased_FirstName+" "+Deceased_Lastname
    RegresstionTestUsers = DataSheetPage(driver)
    RegresstionTestUsers.LoginUsers(hub)

    ID = MyUniqueID(driver)         # Get the Unique ID for the Deceased
    UniqueID = ID.deceasedID(Dname) # Get the Unique ID for the Deceased

    Tracking =TrackingApp(driver)
    if Environment == "local":
        Tracking.local()
    elif Environment =="preprod" :
        Tracking.preprod()
    elif Environment == "qa":
        Tracking.qa()

    bookingin = BookingInPage(driver)
    bookingin.locationName(deceased_sitename)
    bookingin.checkin()

    # Login Page #
    RegresstionTestUsers = DataSheetPage(driver)
    RegresstionTestUsers.LoginUsers(hub)
    bookingin = BookingInPage(driver)

    # Booking Page #
    for elem in driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]'):
        if elem.text == Dname:
            ActionChains(driver).move_to_element(elem).click().perform()
            bookingin.Wristband()
            bookingin.DeceasedintoCare("Released by Family")
            bookingin.AllChecksComplete()
            bookingin.BookIn(UniqueID)
            bookingin.Location()
            RegresstionTestUsers.BookinSecondValidation(hub, UniqueID)      # Second Validation in the Booking in App #
            print("Deceased Booked in Successfully \n")
        else:
            print("Deceased Not available for Booking \n")
        break

@step("I have completed the Mortuary Flow {Deceased_FirstName} {Deceased_Lastname} {Environment} {hub}")
def step_impl(context, Deceased_FirstName, Deceased_Lastname, Environment, hub):

    driver = AutomationDriver.driver

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod" :
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    Dname = Deceased_FirstName+" "+Deceased_Lastname

    RegresstionTestUsers = DataSheetPage(driver)   # Login in the Booking in App
    RegresstionTestUsers.LoginUsers(hub)
    Mortuary = MortuaryPage(driver)
    Mortuary.CreateArrangement(Dname)

    driver.implicitly_wait(50)

    ID = MyUniqueID(driver)                 # Get the Unique ID for the Deceased
    UniqueID = ID.AfterArrangementID()      # NOTE : Here we do not have to Click deceased name as we are
                                            # already in the Arrangement
    Mortuary = MortuaryPage(driver)

    # Joy Ride
    Mortuary.CheckJoyRide()
    # Preparation Tile
    driver.implicitly_wait(30)

    Mortuary.PreparationTile()
    Mortuary.Pacemaker()
    Mortuary.Infectious()
    Mortuary.Gown()
    Mortuary.FingerPrints()
    Mortuary.FingerPrintPermission("Finger Print Permission")
    Mortuary.Embalm()
    Mortuary.EmbalmPermission()
    Mortuary.SavePreparation()

    # Coffin Selection
    Mortuary.CoffinTile()
    Mortuary.StandardCoffin()
    Mortuary.SelectCoffinImage()
    Mortuary.CoffinColour("White")
    Mortuary.SelectCoffin()
    Mortuary.SaveCoffin()

    # Mortuary Flow
    Mortuary.MenuBar()
    Mortuary.CareAndPrep()
    Mortuary.SelectMortuary("East")
    Mortuary.FindDeceased(Dname)
    Mortuary.CareandPrepForm("165")
    Mortuary.SearchDeceased(Dname)
    Mortuary.DressingandCoffin()
    Mortuary.SearchDeceased(Dname)

    Mortuary.Encoffin(hub,UniqueID) # Will take second verification process here
                                    # Also holds Try / Catch
    Mortuary.Logout()

@step("I create an event in the calendar {Deceased_FirstName} {Deceased_Lastname} {Environment} {event_type} {hub}")
def step_impl(context, Deceased_FirstName, Deceased_Lastname, Environment, event_type : str, hub : str):

    driver = AutomationDriver.driver

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod" :
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    Dname = Deceased_FirstName+" "+Deceased_Lastname

    RegresstionTestUsers = DataSheetPage(driver)   # Login in the Booking in App
    RegresstionTestUsers.LoginUsers(hub)

    driver.implicitly_wait(30)

    calendar = CalendarPage(driver)
    calendar.NavBar()
    driver.implicitly_wait(50)
    calendar.CalendarEvent()
    calendar.NewEvent()

    if event_type == "Funeral":
        calendar.FuneralBooking()
    elif event_type == "Staffbooking":
        calendar.StaffBooking()
    elif event_type == "ClientAppointments":
        calendar.ClientBooking()
    elif event_type == "Ceremonialevent":
        calendar.CeremonialEvents()
    elif event_type == "DeceasedVist":
        calendar.DeceasedVisit()
    elif event_type == "AmbulanceDuty":
        calendar.AmbulanceDuty()

    calendar.SelectCategory()

    # Increment todays date by 1 day
    Todaysdate = arrow.now().format('DD/MM/YYYY')
    date1 = datetime.strptime(Todaysdate, "%d/%m/%Y")
    date2 = date1 + timedelta(days=1)
    modified_date = datetime.strftime(date2, "%d/%m/%Y")

    driver.implicitly_wait(10)
    calendar.BookingStartDate(modified_date)
    calendar.BookingStartTime("11:30")
    calendar.BookingEndTime("12:30")
    calendar.DeceasedName(Dname)
    calendar.Burial()
    calendar.Charity1("Charity 1")
    calendar.Charity2("Charity 2")
    calendar.Notes("Notes to be typed here")
    calendar.SaveEvent()  # This function will ensure that available FD is allocated

@then(
    "I completed the booking out Flow {Funeral_Home} {Deceased_FirstName} {Deceased_Lastname} {funeral_type} {Environment} {deceased_sitename} {hub}")
def step_impl(context, Funeral_Home, Deceased_FirstName, Deceased_Lastname, funeral_type, Environment,
              deceased_sitename, hub):

    driver = AutomationDriver.driver

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod":
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    Dname = Deceased_FirstName+" "+Deceased_Lastname
    RegresstionTestUsers = DataSheetPage(driver)   # Login in the Booking in App
    RegresstionTestUsers.LoginUsers(hub)

    ID = MyUniqueID(driver)   # Get the Unique ID for the Deceased
    UniqueID = ID.deceasedID(Dname)

    Tracking =TrackingApp(driver)
    if Environment == "local":
        Tracking.local()
    elif Environment =="preprod" :
        Tracking.preprod()
    elif Environment == "qa":
        Tracking.qa()

    bookingout = BookingOutPage(driver)
    bookingout.locationName(deceased_sitename)
    bookingout.checkout()

    # Login Page #
    RegresstionTestUsers = DataSheetPage(driver)   # Login in the Booking in App
    RegresstionTestUsers.LoginUsers(hub)
    bookingout = BookingOutPage(driver)

    # Booking Out Page #
    for elem in driver.find_elements_by_xpath('.//*[@class = "tap-link__inner__title"]'):
        if elem.text == Dname:
            ActionChains(driver).move_to_element(elem).click().perform()
            bookingout.AllChecksComplete(UniqueID)
            bookingout.PerformFinalChecks()
            bookingout.SecondValidation(hub,UniqueID)  # Second Validation along with other checks

            print("Deceased Booked in Successfully \n")
        else:
            print("Deceased Not available for Booking \n")
        break

@step("Deceased is comitted Successfully {Deceased_FirstName} {Deceased_Lastname} {Environment} {hub}")
def step_impl(context, Deceased_FirstName, Deceased_Lastname, Environment, hub):

    driver = AutomationDriver.driver

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod" :
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    Dname = Deceased_FirstName+" "+Deceased_Lastname
    RegresstionTestUsers = DataSheetPage(driver)   # Login in the Booking in App
    RegresstionTestUsers.LoginUsers(hub)

    driver.find_element_by_link_text(Dname).click()
    driver.find_element_by_id("submit_commit_deceased").click()
    driver.find_element_by_xpath(".//*[@id='dialog-ok']").click()
    try:
        ui.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//*[@class ='message message-success']")))
        elem = driver.find_element_by_xpath(".//*[@class ='message message-success']").text
        if elem.startswith("This deceased was confirmed as committed"):
            print(Dname + " Comitted Successfully")
    except Exception as e: print(Dname + " NOT Comitted. Something went wrong")

    driver.find_element_by_id("close_funeral_arrangement").click()
    driver.find_element_by_id("id_closure_reason_1").click()
    driver.find_element_by_id("submit_close_funeral_arrangement").click()
    driver.find_element_by_xpath(".//*[@id='dialog-ok']").click()

    try:
        ui.WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//*[@class='message message-success']")))
        elem = driver.find_element_by_xpath(".//*[@class='message message-success']").text
        if elem.startswith("You have successfully closed"):
            print(Dname + " Funeral Arrangement Closed Successfully")
    except Exception as e: print(Dname + " Funeral Arrangement Cann Not be Closed")
    driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
    driver.find_element_by_link_text("Log out").click()
