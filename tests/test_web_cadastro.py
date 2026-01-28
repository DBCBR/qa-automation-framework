from faker import Faker
from pages.cadastro_page import CadastroPage

def test_cadastro_com_dados_dinamicos(driver):
    faker = Faker('pt_BR') 
    cadastro = CadastroPage(driver)
    
    # 1. Gerando Massa de Dados
    nome_fake = faker.name()
    cpf_fake = faker.cpf() 
    telefone_fake = faker.cellphone_number() # Gera (XX) 9XXXX-XXXX
    email_fake = faker.email()
    senha_fake = "SenhaForte123!" # Senha pode ser fixa ou faker.password()

    # 2. Ação
    cadastro.abrir() 
    
    # Preenchendo os campos
    cadastro.digitar(cadastro.NOME_FIELD, nome_fake)
    cadastro.digitar(cadastro.CPF_FIELD, cpf_fake)
    cadastro.digitar(cadastro.TELEFONE_FIELD, telefone_fake)
    cadastro.digitar(cadastro.EMAIL_FIELD, email_fake)
    
    fuso_escolhido = "America/Sao_Paulo"
    cadastro.selecionar_fuso_horario(fuso_escolhido)
    
    # Preenchendo as senhas
    cadastro.digitar(cadastro.SENHA_FIELD, senha_fake)
    cadastro.digitar(cadastro.CONFIRM_SENHA_FIELD, senha_fake)
    
    # 3. Finalização
    cadastro.clicar(cadastro.CADASTRAR_BUTTON)
    
    # Aqui entrará a asserção (verificar se cadastrou com sucesso)
    # assert "Sucesso" in driver.page_source