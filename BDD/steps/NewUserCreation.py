from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random
from POM.AutomationDriver import AutomationDriver
from POM.NewUserPage import NewUserPage

use_step_matcher("re")


@given("We have logged in with env")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver
    for row in context.table:
        env =row['environment']

        #base_url = "https://funeral-director-frontend."
        #driver.get(base_url+env+".fnc-dev.co.uk/admin")

        if env == "local":
            driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/admin")
            driver.find_element_by_id("id_username").clear()
            driver.find_element_by_id("id_username").send_keys("admin@admin.com")
            driver.find_element_by_id("id_password").clear()
            driver.find_element_by_id("id_password").send_keys("admin")
        elif env =="preprod" :
            driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/admin")
            driver.find_element_by_id("id_username").clear()
            driver.find_element_by_id("id_username").send_keys("admin@admin.com")
            driver.find_element_by_id("id_password").clear()
            driver.find_element_by_id("id_password").send_keys("PX3TfHt5JxW72mJnpdG7Yr4S")
        elif env == "qa":
            driver.get ("https://funeral-director-frontend-qa.fnc-dev.co.uk/admin")
            driver.find_element_by_id("id_username").clear()
            driver.find_element_by_id("id_username").send_keys("admin@admin.com")
            driver.find_element_by_id("id_password").clear()
            driver.find_element_by_id("id_password").send_keys("admin")

        # driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/admin")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Users").click()


    pass

@then("we create new users using Django Admin")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver

    for row in context.table:
        location = row['location']
        email1   = row['email1']
        username1 = row['username1']
        lastname1 = row['lastname1']
        password1 = row['password1']

        driver.find_element_by_xpath(".//*[@id='content-main']/ul/li/a").click()  # Add User
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(email1)
        driver.find_element_by_id("id_password1").send_keys(password1)

        driver.find_element_by_id("id_password2").send_keys(password1)

        num1 = random.randint(100000, 999999)
        num2 = random.randint(100000, 999999)

        driver.find_element_by_id("id_staffmember-0-uuid").send_keys(num1)
        driver.find_element_by_id("id_staffmember-0-staff_id_number").send_keys(num2)
        driver.find_element_by_id("id_staffmember-0-primary_site").click()
        if location == "edinburgh":
            Select(driver.find_element_by_id("id_staffmember-0-primary_site")).select_by_visible_text("East Newington Place")
            driver.find_element_by_xpath(".//*[@id='id_staffmember-0-secondary_sites']/option[20]").click() # Colinton
        else:
            Select(driver.find_element_by_id("id_staffmember-0-primary_site")).select_by_visible_text("Arden House")
            driver.find_element_by_xpath(".//*[@id='id_staffmember-0-secondary_sites']/option[9]").click() # Bolton

        driver.find_element_by_xpath(".//*[@id='id_staffmember-0-capabilities']/option[8]").click()
        driver.find_element_by_id("id_staffmember-0-contracted_hours_per_week").send_keys("37.5")
        driver.find_element_by_name("_continue").click()

        driver.find_element_by_id("id_first_name").send_keys(username1)
        driver.find_element_by_id("id_last_name").send_keys(lastname1)
        driver.find_element_by_id("id_email").send_keys(email1)
        driver.find_element_by_xpath(".//*[@id='id_groups']/option[4]").click()
        #driver.find_element_by_name("_continue").click()
        driver.find_element_by_xpath(".//*[@id='user_form']/div/div[2]/input[1]").click()

        # def is_element_present(self, how, what):
        #     try: driver.find_element(by=how, value=what)
        #     except NoSuchElementException as e: return False
        #     return True
        #
        # # bodyText = driver.find_element_by_tag_name('body').text
        # # assert ("the text you want to check for" in bodyText)


    elem = driver.find_element_by_xpath(".//*[@id='header']/div[2]/a[3]")
    ActionChains(driver).move_to_element(elem).click().perform()



@given("I have required login detail from user created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver
    for row in context.table:
        environment = row['environment']
        email1      = row['email1']
        password1   = row['password1']

        driver = AutomationDriver.driver
        #base_url = "https://funeral-director-frontend."
        #driver.get(base_url + environment +".fnc-dev.co.uk/credentials/login/?next=/")
        driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/credentials/login/?next=/")
        if environment == "local":
            driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next=/")
        elif environment =="preprod" :
            driver.get("https://funeral-director-frontend-preprod.fnc-tools.co.uk/credentials/login/?next=/")
        elif environment == "qa":
            driver.get ("https://funeral-director-frontend-qa.fnc-dev.co.uk/credentials/login/?next=/")


        driver.maximize_window()
        driver.implicitly_wait(30)

        driver.find_element_by_id("id_username").send_keys(email1)
        driver.find_element_by_id("id_password").send_keys(password1)
        driver.find_element_by_xpath("//input[@value='Login']").click()
    pass


@then("I create all the Users")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver

    for row in context.table:
        location    = row['location']
        email      = row['email']
        username2   = row['username2']
        lastname2   = row['lastname2']
        role        = row['role']

        colleagueid = random.randint(100000, 999999)
        num1 = random.randint(1000000000, 9999999999)

        driver.find_element_by_id("side_nav_staff_admin_list_view").click()
        driver.find_element_by_id("add_user").click()
        driver.find_element_by_id("id_user-email").send_keys(email)
        driver.find_element_by_id("id_user-first_name").send_keys(username2)
        driver.find_element_by_id("id_user-last_name").send_keys(lastname2)
        driver.find_element_by_id("id_staff_member-primary_mobile_number").send_keys(num1)

        newuser = NewUserPage(driver)

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

        driver.find_element_by_id("id_staff_member-staff_id_number").send_keys(colleagueid)

        ################ PRIMARY SITE ####################

        if location == "edinburgh" :
            newuser.sitelocation("Lothian Road")
        else:
            newuser.sitelocation("Arden House")

        ################ SECONDARY SITE ##################

        if location == "edinburgh" :
            newuser.SecondarySite("Colinton")
            newuser.SecondarySite("Gilmerton")
            newuser.SecondarySite("Morningside")
            newuser.SecondarySite("South Clerk Street")
            newuser.SecondarySite("Ferry Road")
            newuser.SecondarySite("Queensferry Road")
            newuser.SecondarySite("East Newington Place")
            newuser.SecondarySite("Corstorphine")
            newuser.SecondarySite("Leith")
            newuser.SecondarySite("Piershill")

        else:
            newuser.SecondarySite("Horwich")
            newuser.SecondarySite("Chorley Old Rd")
            newuser.SecondarySite("Hall and Heyes")
            newuser.SecondarySite("Relphs")
            newuser.SecondarySite("Bolton")
            newuser.SecondarySite("Farnworth")
            newuser.SecondarySite("Shaw & Son")
            newuser.SecondarySite("Hardman and McManus")
            newuser.SecondarySite("Worthingtons")
            newuser.SecondarySite("Cheethams")


        newuser.ContractedHours("37.5")
        driver.find_element_by_id("save-progress").click()

        ############### Add more capabilities ##############

        driver.find_element_by_id("side_nav_staff_admin_list_view").click()
        driver.find_element_by_link_text(email).click()

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

        if role == "FD":
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[8]").click()
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[11]").click()
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[12]").click()
        elif role == "FSO":
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()
        elif role == "LM":
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()
        elif role == "mortuary":
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()
        elif role == "RM":
            driver.find_element_by_xpath(".//*[@id='id_staff_member-capabilities']/option[9]").click()

            # driver.find_element_by_id("save-progress").click()
    driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
    driver.find_element_by_link_text("Log out").click()
pass


@then("I generate passwords for all the users created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver = AutomationDriver.driver

    for row in context.table:
        email = row['email']
        password = row['password']
        username = row['username']
        lastname = row['lastname']

        name = username + " " + lastname

        driver.find_element_by_id("searchbar").clear()
        driver.find_element_by_id("searchbar").send_keys(email)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text(name).click()
        driver.find_element_by_link_text("this form").click()

        driver.find_element_by_id("id_password1").send_keys(password)
        driver.find_element_by_id("id_password2").send_keys(password)

        driver.find_element_by_css_selector("input.default").click()
        driver.find_element_by_name("_save").click()

    elem = driver.find_element_by_xpath(".//*[@id='header']/div[2]/a[3]")
    ActionChains(driver).move_to_element(elem).click().perform()


