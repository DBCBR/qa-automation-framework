from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class CadastroPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Locators da Página de Cadastro
        self.BANDEIRA_BR = (
            By.CSS_SELECTOR, "button[aria-label='Mudar idioma para Português']")
        self.NOME_FIELD = (By.NAME, "username")
        self.CPF_FIELD = (By.NAME, "cpf")
        self.TELEFONE_FIELD = (By.NAME, "contact")
        self.FUSO_HORARIO_INPUT = (By.CSS_SELECTOR, "input[role='combobox']")
        self.EMAIL_FIELD = (By.NAME, "email")
        self.SENHA_FIELD = (By.NAME, "password")
        self.CONFIRM_SENHA_FIELD = (By.NAME, "confirmPassword")
        # Locator do botão Cadastrar (com texto dinâmico)
        self.CADASTRAR_BUTTON = (
            By.XPATH, "//*[text()='Cadastrar' or contains(text(), 'Cadastrar')]/ancestor-or-self::button")
        # Locators para confirmação de código via e-mail
        self.CODIGO_CONFIRMACAO_FIELD = (By.CSS_SELECTOR, "input[placeholder='000000']")
        
        self.REENVIAR_CODIGO_BUTTON = (By.XPATH, "//button[contains(., 'Reenviar código')]")
        
        self.CONFIRMAR_CODIGO_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    # Ações Específicas da Página de Cadastro
    def abrir(self):
        self.driver.get("https://goams-frontend.fly.dev/LoginPage")

    def mudar_para_portugues(self):
        self.clicar(self.BANDEIRA_BR)
        # Aguarda um breve momento para o React processar a tradução
        import time
        time.sleep(1)
    # Função para selecionar fuso horário

    def get_locator_fuso(self, nome_fuso):
        return (By.XPATH, f"//li[@role='option']//*[contains(text(), '{nome_fuso}')] | //li[@role='option'][contains(text(), '{nome_fuso}')]")

    def selecionar_fuso_horario(self, texto_busca):
        self.clicar(self.FUSO_HORARIO_INPUT)
        self.digitar(self.FUSO_HORARIO_INPUT, texto_busca)
        # Força um ENTER caso a lista demore
        from selenium.webdriver.common.keys import Keys
        self.encontrar_elemento(self.FUSO_HORARIO_INPUT).send_keys(Keys.ENTER)
