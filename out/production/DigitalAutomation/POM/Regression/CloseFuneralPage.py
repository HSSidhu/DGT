from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui


class CloseFuneralPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def CommitDeceased(self, Dname):
        self.driver.find_element_by_link_text(Dname).click()
        self.driver.find_element_by_id("submit_commit_deceased").click()
        self.driver.find_element_by_xpath(".//*[@id='dialog-ok']").click()
        try:
            ui.WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//*[@class ='message message-success']")))
            elem = self.driver.find_element_by_xpath(".//*[@class ='message message-success']").text
            if elem.startswith("This deceased was confirmed as committed"):
                print(Dname + " Comitted Successfully")
        except Exception as e: print(Dname + " NOT Comitted. Something went wrong")

    def CloseArrangement(self, Dname):
        self.driver.find_element_by_id("close_funeral_arrangement").click()
        self.driver.find_element_by_id("id_closure_reason_1").click()
        self.driver.find_element_by_id("submit_close_funeral_arrangement").click()
        self.driver.find_element_by_xpath(".//*[@id='dialog-ok']").click()

        try:
            ui.WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, ".//*[@class='message message-success']")))
            elem = self.driver.find_element_by_xpath(".//*[@class='message message-success']").text
            if elem.startswith("You have successfully closed"):
                print(Dname + " Funeral Arrangement Closed Successfully")
        except Exception as e: print(Dname + " Funeral Arrangement Cann Not be Closed")
        self.driver.find_element_by_css_selector("button.menu-toggle__nav.menu-toggle__nav--user").click()
        self.driver.find_element_by_link_text("Log out").click()

