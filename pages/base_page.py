from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def encontrar_elemento(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def clicar(self, locator):
        elemento = self.encontrar_elemento(locator)
        try:
            # Tenta o clique normal do Selenium primeiro
            elemento.click()
        except Exception:
            # Se der erro de interceptação ou qualquer outro, usa o JS como "Plano B"
            print(f"[DEBUG] Clique normal falhou para {locator}, tentando via JS...")
            self.driver.execute_script("arguments[0].click();", elemento)
        
    def digitar(self, locator, texto):
        self.encontrar_elemento(locator).send_keys(texto)
