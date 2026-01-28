from selenium.webdriver.common.by import By
from pages.base_page import BasePage # Importa a base

class LoginPage(BasePage): # Herda da BasePage
    def __init__(self, driver):
        super().__init__(driver) # Inicializa o driver e o wait da base
        self.url = "https://goams-frontend.fly.dev/LoginPage"

        self.USERNAME_FIELD = (By.ID, "user-name")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")
        
    def abrir(self):
        self.driver.get(self.url)
        
    def fazer_login(self, username, password):
        self.digitar(self.USERNAME_FIELD, username)
        self.digitar(self.PASSWORD_FIELD, password)
        self.clicar(self.LOGIN_BUTTON) # Usando a base page para reutilizar métodos comuns