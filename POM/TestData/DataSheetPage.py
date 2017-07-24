import xlrd

from POM.Helpers.LoginPage import LoginPage
from POM.Regression.BookingInPage import BookingInPage


class DataSheetPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def LoginUsers(self, hub):
        self.TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
        AllUsers = self.TestData.sheet_by_name("RegressionTesting")

        if hub == "Edinburgh":
            email = AllUsers.cell_value(1,0)
            password = AllUsers.cell_value(1,2)

        else:
            email = AllUsers.cell_value(2,0)
            password = AllUsers.cell_value(2,2)

        t = LoginPage(self.driver)  # using another function
        t.UserName(email)
        t.Password(password)

    def BookinSecondValidation(self, hub, UniqueID):
        self.TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
        AllUsers = self.TestData.sheet_by_name("RegressionTesting")

        if hub == "Edinburgh":
            email = AllUsers.cell_value(1,1)
            password = AllUsers.cell_value(1,2)

        else:
            email = AllUsers.cell_value(2,1)
            password = AllUsers.cell_value(2,2)

        t = BookingInPage(self.driver)  # using another function
        t.SecondValidation(email, password, UniqueID)

    def BookOUTSecondValidation(self, hub):
        self.TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
        AllUsers = self.TestData.sheet_by_name("RegressionTesting")

        if hub == "Edinburgh":
            email = AllUsers.cell_value(1,1)
            password = AllUsers.cell_value(1,2)

        else:
            email = AllUsers.cell_value(2,1)
            password = AllUsers.cell_value(2,2)

        self.driver.find_element_by_id("id_second_verification-second_user_email").send_keys(email)
        self.driver.find_element_by_id("id_second_verification-second_user_password").send_keys(password)


    def MortuarySecondValidation(self, hub):
        self.TestData = xlrd.open_workbook("F:\\AUTOMATION\\ALLCompletedProjects\\Python\\VM\\TestData.xlsx")
        AllUsers = self.TestData.sheet_by_name("RegressionTesting")

        if hub == "Edinburgh":
            email = AllUsers.cell_value(1,1)
            password = AllUsers.cell_value(1,2)

        else:
            email = AllUsers.cell_value(2,1)
            password = AllUsers.cell_value(2,2)

        self.driver.find_element_by_id("id_username").send_keys(email)
        self.driver.find_element_by_id("id_password").send_keys(password)






