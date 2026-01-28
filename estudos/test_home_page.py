from estudos.home_page import HomePage

def test_obter_titulo(driver):
    home_page = HomePage(driver)
    home_page.abrir()
    assert "Petrobras" in home_page.obter_titulo()
    
def test_naveagacao_hq(driver):
    home_page = HomePage(driver)
    home_page.abrir()
    hq_page = home_page.clicar_link_historia_quadrinhos()
    assert "Histórias em Quadrinhos" in hq_page.obter_titulo()
    
    url_esperada = "https://petrobras.com.br/transicao-energetica/historias-em-quadrinhos"
    assert url_esperada == hq_page.obter_url_atual()