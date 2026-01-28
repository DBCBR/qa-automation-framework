import requests
import pytest

def test_get_user(base_url, headers):
    response = requests.get(f"{base_url}/user", headers=headers)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert users 
    first_user = users[0]
    expected_keys = {"cognito_id", "username", "email"}
    assert expected_keys.issubset(first_user)

def test_create_process(base_url, headers):
    new_process = {
        "name": "Automação de Teste",
        "description": "Automatiza o processo de teste",
        "cognito_id": "f80133a0-30d1-7041-1b13-8db3b75eabf5",
        "company_cnpj": "57929932000130",
        "setor": "TI",
        "max_processes": 50,
        "created_by": "f80133a0-30d1-7041-1b13-8db3b75eabf5",
        "updated_by": "f80133a0-30d1-7041-1b13-8db3b75eabf5"
    }
    response = requests.post(f"{base_url}/process", json=new_process, headers=headers)
    
    assert response.status_code == 201
    created_process = response.json()
    
    # Valida se os campos enviados estão no retorno
    for key in new_process:
        assert created_process[key] == new_process[key]
    
    # Validações com os nomes reais da API
    assert "process_id" in created_process
    assert "createdAt" in created_process
    assert "updatedAt" in created_process

def test_get_process(base_url, headers):
    cognito_id = "f80133a0-30d1-7041-1b13-8db3b75eabf5"
    # Rota corrigida para Path Parameter
    response = requests.get(f"{base_url}/process/{cognito_id}", headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    
    # Acessando a lista dentro de 'items'
    assert "items" in data
    processes = data["items"]
    assert isinstance(processes, list)
    assert len(processes) > 0
    
    # Validando o primeiro processo retornado
    first_process = processes[0]
    assert first_process["cognito_id"] == cognito_id
    assert "process_id" in first_process
       
def test_bug_integridade_usuario_empresa(base_url, headers):
    url = f"{base_url}/user"
    payload = {
        "cognito_id": "", # Deixando em branco como você testou
        "username": "Cristiano Ronaldo",
        "email": "cr7@gmail.com",
        "cpf": "12345678900",
        "company_cnpj": "57929932000130", # CNPJ que você sabe que existe
        "role": "Executor"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    # Se o bug de integridade ainda existe, o teste falha aqui com uma mensagem clara
    assert response.status_code != 500, (
        f"FALHA DE INTEGRIDADE DETECTADA: O banco rejeitou a criação mesmo com empresa existente. "
        f"Resposta: {response.text}"
    )