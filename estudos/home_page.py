from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from estudos.hq_page import HqPage

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.petrobras.com.br/"
        
    def abrir(self):
        self.driver.get(self.url)
        
    def obter_titulo(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(
        "Petrobras"
        ))
        return self.driver.title

    def clicar_link_historia_quadrinhos(self, timeout=10):
        elemento = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "HISTÓRIAS EM QUADRINHOS")))
        elemento.click()
        return HqPage(self.driver)