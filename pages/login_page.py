from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        
    def abrir(self):
        self.driver.get(self.url)
        
    def obter_titulo(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(
        "Swag Labs"
        ))
        return self.driver.title
    
    def fazer_login(self, username, password, timeout=10):
        username_input = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(
            (By.ID, "user-name")))
        password_input = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(
            (By.ID, "password")))
        login_button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(
            (By.ID, "login-button")))
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()