from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def encontrar_elemento(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def clicar(self, locator):
        self.encontrar_elemento(locator).click()
        
    def digitar(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)
