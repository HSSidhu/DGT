import random

import xlrd
from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

from POM.Helpers.AutomationDriver import AutomationDriver
from POM.Helpers.LoginPage import LoginPage
from POM.Helpers.MainApp import MainApp
from POM.NewUser.AdminLoginPage import AdminLoginPage
from POM.NewUser.DjangoPage import DjangoPage
from POM.NewUser.NewUserPage import NewUserPage

use_step_matcher("re")


@given("We have logged in with env")
def step_impl(context):

    driver = AutomationDriver.driver

    TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
    AllUsers = TestData.sheet_by_name("Admin")

    Environment = AllUsers.cell_value(1,0) # will always have value selected from ADMIMN sheet Row / Colum 0

    AdminLogin = AdminLoginPage(driver)
    if Environment == "local":
        AdminLogin.local()
    elif Environment =="preprod" :
        AdminLogin.preprod()
    elif Environment == "qa":
        AdminLogin.qa()

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector("input[type=\"submit\"]").click()
    driver.find_element_by_link_text("Users").click()

@then("we create new users using Django Admin")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver


    TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
    AllUsers = TestData.sheet_by_name("Admin")
    AdminUsers = DjangoPage(driver)
    for row in range (AllUsers.nrows):
        num1 = random.randint(100000, 999999)
        num2 = random.randint(100000, 999999)
        if row == 0:
            a= 1
        else :
            location = AllUsers.cell_value(row, 1)
            email1   = AllUsers.cell_value(row, 2)
            username1 = AllUsers.cell_value(row, 3)
            lastname1 = AllUsers.cell_value(row, 4)
            password1 = AllUsers.cell_value(row, 5)

            AdminUsers.EnterUserDetails(email1,password1, num1, num2, location)
            AdminUsers.ReEnterDetails(username1, lastname1, email1)

    AdminUsers.Logout()

@given("I have required login detail from user created (?P<Location>.+)")
def step_impl(context, Location):

    driver = AutomationDriver.driver
    TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
    AllUsers = TestData.sheet_by_name("Admin")

    if Location == "Edinburgh" :
        Environment = AllUsers.cell_value(1, 0)
        email   = AllUsers.cell_value(1, 2)
        username1 = AllUsers.cell_value(1, 3)
        lastname1 = AllUsers.cell_value(1, 4)
        password = AllUsers.cell_value(1, 5)

    else :
        Environment = AllUsers.cell_value(2, 0)
        email  = AllUsers.cell_value(2, 2)
        username1 = AllUsers.cell_value(2, 3)
        lastname1 = AllUsers.cell_value(2, 4)
        password = AllUsers.cell_value(2, 5)

    mainapp = MainApp(driver)
    if Environment == "local":
        mainapp.local()
    elif Environment =="preprod" :
        mainapp.preprod()
    elif Environment == "qa":
        mainapp.qa()

    driver.maximize_window()
    driver.implicitly_wait(30)

    login= LoginPage(driver)
    login.UserName(email)
    login.Password(password)

@then("I create all the Users (?P<Location>.+)")
def step_impl(context, Location):

    driver = AutomationDriver.driver
    newuser = NewUserPage(driver)
    newuser.OpenMenuLink()
    TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
    if Location == "Edinburgh":
        AllUsers = TestData.sheet_by_name("EdinNewUsers")
    else:
        AllUsers = TestData.sheet_by_name("BoltonNewuser")

    for rows in range(AllUsers.nrows):
        colleagueid = random.randint(100000, 999999)
        num1 = random.randint(1000000000, 9999999999)
        if rows == 0 :
            a= 1
        else:
            email      = AllUsers.cell_value(rows, 1)
            username2  = AllUsers.cell_value(rows, 2)
            lastname2  = AllUsers.cell_value(rows, 3)
            role       = AllUsers.cell_value(rows, 4)

            newuser.AddUserLink(email,username2,lastname2,num1, colleagueid)

            if role == "FD":
                F_Role = "Funeral director"
                newuser.UserRole(F_Role)
            elif role == "FSO":
                F_Role = "Funeral service operative"
                newuser.UserRole(F_Role)
            elif role == "LM":
                F_Role = "Logistics manager"
                newuser.UserRole(F_Role)
            elif role == "mortuary":
                F_Role = "Mortuary staff"
                newuser.UserRole(F_Role)
            elif role == "RM":
                F_Role = "Regional manager"
                newuser.UserRole(F_Role)

            # ADD SITE

            if Location == "Edinburgh" :
                newuser.sitelocation("Lothian Road")
                newuser.SecondarySite("Colinton")               # SECONDARY SITE
                newuser.SecondarySite("Gilmerton")              # SECONDARY SITE
                newuser.SecondarySite("Morningside")            # SECONDARY SITE
                newuser.SecondarySite("South Clerk Street")     # SECONDARY SITE
                newuser.SecondarySite("Ferry Road")             # SECONDARY SITE
                newuser.SecondarySite("Queensferry Road")       # SECONDARY SITE
                newuser.SecondarySite("East Newington Place")   # SECONDARY SITE
                newuser.SecondarySite("Corstorphine")           # SECONDARY SITE
                newuser.SecondarySite("Leith")                  # SECONDARY SITE
                newuser.SecondarySite("Piershill")              # SECONDARY SITE
            else:
                newuser.sitelocation("Arden House")
                newuser.SecondarySite("Horwich")                # SECONDARY SITE
                newuser.SecondarySite("Chorley Old Rd")         # SECONDARY SITE
                newuser.SecondarySite("Hall and Heyes")         # SECONDARY SITE
                newuser.SecondarySite("Relphs")                 # SECONDARY SITE
                newuser.SecondarySite("Bolton")                 # SECONDARY SITE
                newuser.SecondarySite("Farnworth")              # SECONDARY SITE
                newuser.SecondarySite("Shaw & Son")             # SECONDARY SITE
                newuser.SecondarySite("Hardman and McManus")    # SECONDARY SITE
                newuser.SecondarySite("Worthingtons")           # SECONDARY SITE
                newuser.SecondarySite("Cheethams")              # SECONDARY SITE

            newuser.ContractedHours("37.5")
            newuser.SaveNewUserDetails()

            try:
                ui.WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "message-content")))
                elem = driver.find_element_by_class_name("message-content").text
                if elem.startswith("You have successfully created"):
                    print("Colleague Created Successfully \n")
            except TimeoutException as e: print("Colleague Could not be created. Please look into this")

        ############### Add more capabilities ##############

            newuser.FindUser(email)
            if role == "FD":
                newuser.FDCapabilities()
            elif role == "FSO":
                newuser.FSOcapabilities()
            elif role == "LM":
                newuser.LMCapabilities()
            elif role == "mortuary":
                newuser.MortuaryCapabilities()
            elif role == "RM":
                newuser.RMCapabilities()

            newuser.SaveNewUserDetails()
    newuser.Logout()


@then("I generate passwords for all the users created")
def step_impl(context):
    driver = AutomationDriver.driver
    newuser = NewUserPage(driver)

    TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
    AllUsers = TestData.sheet_by_name("AllNewUsers")

    for rows in range(AllUsers.nrows):
        if rows == 0 :
            a= 1
        else:
            email = AllUsers.cell_value(rows, 1)
            username = AllUsers.cell_value(rows, 2)
            lastname = AllUsers.cell_value(rows, 3)
            password = AllUsers.cell_value(rows, 5)

            name = username + " " + lastname
            newuser.ResetPassword(email,name, password)

    elem = driver.find_element_by_xpath(".//*[@id='header']/div[2]/a[3]")
    ActionChains(driver).move_to_element(elem).click().perform()
