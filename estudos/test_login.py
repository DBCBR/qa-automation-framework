from pages.login_page import LoginPage

def test_obter_titulo(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    assert "Swag Labs" in login_page.obter_titulo()
    
def test_fazer_login_com_sucesso(driver):
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.fazer_login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url