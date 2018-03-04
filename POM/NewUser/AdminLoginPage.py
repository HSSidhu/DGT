class AdminLoginPage(object):

    def __init__(self,AutomationDriver):
        self.driver= AutomationDriver

    def local(self):
        self.driver.get("https:-dev.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("admin")

    def preprod(self):
        self.driver.get("https://tools.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("admin")

    def qa(self):
        self.driver.get ("https:dev.co.uk/admin")
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("admin")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("admin")
        
        
