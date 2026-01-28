import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Carrega o .env uma única vez para todo o projeto
load_dotenv()

@pytest.fixture(scope="session")
def headers():
    """Retorna os headers padrão para chamadas de API"""
    api_key = os.getenv("x-tenant-api-key")
    return {
        "x-tenant-api-key": api_key,
        "Content-Type": "application/json"
    }

@pytest.fixture(scope="session")
def base_url():
    """Retorna a URL base da API"""
    return "https://goams-backend.fly.dev"

@pytest.fixture(scope="class")
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    yield driver
    driver.quit()

