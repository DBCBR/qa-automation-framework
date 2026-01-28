import pytest
import time
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cadastro_page import CadastroPage
from utils.email_helper import EmailHelper


def test_cadastro_com_dados_dinamicos(driver):
    faker = Faker('pt_BR')
    cadastro = CadastroPage(driver)
    email_tool = EmailHelper()

    # 1. Gerando Massa de Dados
    nome_fake = faker.name()
    cpf_fake = faker.cpf()
    telefone_fake = faker.cellphone_number()
    # No test_web_cadastro.py
    email_para_uso = email_tool.gerar_email_temporario("user_qa_david")
    senha_fake = "SenhaForte123!"

    # 2. Ação no Navegador
    cadastro.abrir()

    # 3. Garantir Idioma
    cadastro.mudar_para_portugues()

    # Preenchendo os campos
    cadastro.digitar(cadastro.NOME_FIELD, nome_fake)
    cadastro.digitar(cadastro.CPF_FIELD, cpf_fake)
    cadastro.clicar(cadastro.TELEFONE_FIELD)
    cadastro.digitar(cadastro.TELEFONE_FIELD, telefone_fake)
    cadastro.digitar(cadastro.EMAIL_FIELD, email_para_uso)

    fuso_escolhido = "America/Sao_Paulo"
    cadastro.selecionar_fuso_horario(fuso_escolhido)

    # Preenchendo as senhas
    cadastro.digitar(cadastro.SENHA_FIELD, senha_fake)
    cadastro.digitar(cadastro.CONFIRM_SENHA_FIELD, senha_fake)

    # 4. Finalização do Primeiro Passo
    cadastro.clicar(cadastro.CADASTRAR_BUTTON)

    # Espera a mensagem de sucesso aparecer na tela
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), "Usuário criado com sucesso!")
    )

    # 5. Captura do Código de Confirmação via E-mail
    # O robô agora para e fica checando a caixa de entrada do Mailsac

    # ... captura do código via e-mail ...
    codigo_recebido = email_tool.esperar_pelo_codigo(email_para_uso)

    if codigo_recebido:
        print(f"\n[PAUSE] Código {codigo_recebido} capturado.")
        
        # Opcional: Remova o breakpoint depois que validar que o seletor funcionou
        # breakpoint() 

        # Digita o código no campo com placeholder
        cadastro.digitar(cadastro.CODIGO_CONFIRMACAO_FIELD, codigo_recebido)
        
        # ESPERA DE SEGURANÇA: Dá tempo para o botão habilitar
        time.sleep(1) 
        
        # AQUI ESTÁ A MÁGICA: Clique via JavaScript para evitar a interceptação
        try:
            cadastro.clicar_js(cadastro.CONFIRMAR_CODIGO_BUTTON)
        except:
            # Caso o JS click falhe, tentamos um Enter direto no campo
            from selenium.webdriver.common.keys import Keys
            cadastro.encontrar_elemento(cadastro.CODIGO_CONFIRMACAO_FIELD).send_keys(Keys.ENTER)

        # Validação final de sucesso
        time.sleep(3)
        assert "LoginPage" in driver.current_url
