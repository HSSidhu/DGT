from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import LoginPage

driver = webdriver.Chrome("F:\\AUTOMATION\\Browsers\\Chrome\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()
driver.get("http://funeral-director-frontend.local.fnc-dev.co.uk/credentials/login/?next=/")
assert "Co-op Funeralcare" in driver.title


Login = LoginPage(driver)
Login.UserName("harwinder.sidhu@coopdigital.co.uk")
Login.Password("password")




NewCall = driver.find_element_by_id("new_call")
NewCall.send_keys(Keys.RETURN)

#### FIRST CALL####
CallerTitle = driver.find_element_by_id("select2-id_first_contact-client_title-container")
CallerFirstName = driver.find_element_by_name("first_contact-client_first_name")
CallerLastName = driver.find_element_by_name("first_contact-client_last_name")
CallerTelephone = driver.find_element_by_id("id_first_contact-client_telephone_number")
CallerMobile = driver.find_element_by_id("id_first_contact-client_mobile_telephone_number")
CallerMainContact = driver.find_element_by_id("id_first_contact-client_main_contact_0")
CallerRelationship = driver.find_element_by_id("select2-id_first_contact-client_relationship-container")
FuneralHome = driver.find_element_by_id("select2-id_first_contact-funeral_home-container")
DeceasedFirstName = driver.find_element_by_id("id_deceased-first_name")
DeceasedLastName = driver.find_element_by_id("id_deceased-last_name")
DeceasedDOD = driver.find_element_by_id("id_deceased-date_of_death")
DeceasedDOB = driver.find_element_by_id("id_deceased-date_of_birth")
Burial = driver.find_element_by_id("id_first_contact-burial_cremation_1")
Cremation = driver.find_element_by_id("id_first_contact-burial_cremation_2")
DeceasedDeathverifiedYes = driver.find_element_by_id("id_deceased-verification_of_death_0")
deceasedDeathverifiedNo = driver.find_element_by_id("id_deceased-verification_of_death_1")
DeceasedDeathRegisteredYes = driver.find_element_by_id("id_deceased-registration_of_death_1")
DeceasedDeathRegisteredNo = driver.find_element_by_id("id_deceased-registration_of_death_2")
DeceasedAddress1 = driver.find_element_by_id("id_first_contact-place_of_death_address_line_one")
DeceasedcollectionYes = driver.find_element_by_id("id_first_contact-book_collection_now_1")
DeceasedresidenceDomestic = driver.find_element_by_id("id_first_contact-collection_type_of_residence_1")
DeceasedresidenceHospital = driver.find_element_by_id("id_first_contact-collection_type_of_residence_2")
DeceasedresidenceHospice = driver.find_element_by_id("id_first_contact-collection_type_of_residence_3")
DeceasedresidenceNursingHome = driver.find_element_by_id("id_first_contact-collection_type_of_residence_4")
DeceasedsamePOD = driver.find_element_by_id("id_first_contact-collection_same_as_place_of_death")
Deceasedappointment = driver.find_element_by_id("id_first_contact-appointment_book_0")


#### FIRST CALL - Enter Details####
CallerTitle.click()
driver.find_element_by_class_name("select2-search__field").send_keys("Mr")
driver.find_element_by_class_name("select2-results__option").click()

CallerFirstName.send_keys("Molly")
CallerLastName.send_keys("Miller")
CallerTelephone.send_keys("01234567891")
CallerMobile.send_keys("09876543211")

CallerRelationship.click()
driver.find_element_by_class_name("select2-search__field").send_keys("Aunt")
driver.find_element_by_class_name("select2-results__option").click()

CallerMainContact.click()

FuneralHome.click()
driver.find_element_by_class_name("select2-search__field").send_keys("Colinton")
driver.find_element_by_class_name("select2-results__option").click()

DeceasedFirstName.send_keys("Benny")
DeceasedLastName.send_keys("Dore")
DeceasedDOB.send_keys("01/01/1955")
DeceasedDOD.send_keys("01/01/2017")




