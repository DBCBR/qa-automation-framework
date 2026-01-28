import pytest
from selenium import webdriver

# @pytest.fixture
# def titulo_esperado():
#     return "O Brasil é a nossa Energia | Petrobras"

# def test_titulo_petrobras(titulo_esperado):
#     assert "O Brasil é a nossa Energia | Petrobras" == titulo_esperado
    
    
# @pytest.fixture
# def recurso():
#     print("Setup do recurso")
#     yield "ativo"
#     print("Teardown do recurso")
    
# def test_recurso(recurso):
#     assert recurso == "ativo"

# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     print("Setup do driver")
#     yield driver
#     driver.quit()
    
# def test_driver(driver):
#     driver.get("https://www.petrobras.com.br/")
#     assert driver.title == "O Brasil é a nossa Energia | Petrobras"
    

    
# def test_driver2(driver):
#     driver.get("https://www.petrobras.com.br/")
#     assert driver.title == "O Brasil é a nossa Energia | Petrobras"
   
class TestPetrobras:
    def test_driver(self, driver):
        driver.get("https://www.petrobras.com.br/")
        assert driver.title == "O Brasil é a nossa Energia | Petrobras"
    
    def test_driver2(self, driver):
        driver.get("https://www.petrobras.com.br/")
        assert driver.title == "O Brasil é a nossa Energia | Petrobras"
