from pages.login_page import LoginPage

def test_login_com_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    
    login_page.fazer_login("usuario_teste", "senha_teste")    
    # Aqui você pode adicionar asserções para verificar se o login foi bem-sucedido
    