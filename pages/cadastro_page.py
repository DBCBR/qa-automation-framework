from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class CadastroPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.NOME_FIELD = (By.NAME, "username")
        self.CPF_FIELD = (By.NAME, "cpf")
        self.TELEFONE_FIELD = (By.NAME, "contact")
        self.FUSO_HORARIO_INPUT = (By.CSS_SELECTOR, "input[role='combobox']")
        self.EMAIL_FIELD = (By.NAME, "email")
        self.SENHA_FIELD = (By.NAME, "password")
        self.CONFIRM_SENHA_FIELD = (By.NAME, "confirmPassword")
                
        self.CADASTRAR_BUTTON = (By.NAME, "Cadastrar")

    def selecionar_fuso_horario(self, texto_busca):
        self.digitar(self.FUSO_HORARIO_INPUT, texto_busca)
        locator_opcao = self.get_locator_fuso(texto_busca)
        self.clicar(locator_opcao)
        # self.encontrar_elemento(self.FUSO_HORARIO_INPUT).send_keys(Keys.ENTER)
        
    def get_locator_fuso(self, nome_fuso):
        return (By.XPATH, f"//li[@role='option' and contains(text(), '{nome_fuso}')]")
    
    def abrir(self):
        self.driver.get("https://goams-frontend.fly.dev/LoginPage")