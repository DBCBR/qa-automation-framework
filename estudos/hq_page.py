from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HqPage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://petrobras.com.br/transicao-energetica/historias-em-quadrinhos"
        
    def abrir(self):
        self.driver.get(self.url)
        
    def obter_titulo(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.title_contains(
        "Quadrinhos"
        ))
        return self.driver.title
    
    def obter_url_atual(self):
        return self.driver.current_url