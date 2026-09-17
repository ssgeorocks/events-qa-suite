from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    url = "/login.html"

    _EMAIL = (By.ID, "email")
    _PASSWORD = (By.ID, "password")
    _SUBMIT = (By.ID, "btnLogin")

    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(f"{self.base_url}{self.url}")
        self.wait.until(EC.visibility_of_element_located(self._EMAIL))
        return self

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self._EMAIL)).send_keys(email)
        self.driver.find_element(*self._PASSWORD).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT)).click()
        return self
