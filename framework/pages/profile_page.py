from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    _LOGOUT = (By.ID, "logoutBtn")
    _NAME   = (By.ID, "profileName")
    _EMAIL  = (By.ID, "profileEmail")
    _ROLE   = (By.ID, "profileRole")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_page(self):
        self.wait.until(EC.presence_of_element_located(self._EMAIL))
        return self

    @property
    def name(self):
        return self.driver.find_element(*self._NAME).text

    @property
    def email(self):
        return self.driver.find_element(*self._EMAIL).text

    @property
    def role(self):
        return self.driver.find_element(*self._ROLE).text
