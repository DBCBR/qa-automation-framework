# QA Automation Framework 🚀

Este repositório hospeda um framework de automação de testes unificado, abrangendo camadas de **API** e **Web (UI)**. O projeto foi arquitetado com foco em escalabilidade, manutenibilidade e alta confiabilidade, utilizando as melhores práticas de engenharia de software aplicadas ao teste.

## 🎯 Objetivo do Projeto

Validar a integridade funcional e de dados da plataforma GoAMS, automatizando desde o contrato de APIs até fluxos críticos de interface, garantindo que regressões sejam detectadas de forma precoce no ciclo de desenvolvimento.

## 🛠 Stack Tecnológica

- **Linguagem:** [Python 3.14+](https://www.python.org/)
- **Test Runner:** [Pytest](https://docs.pytest.org/)
- **Automação Web:** [Selenium WebDriver](https://www.selenium.dev/)
- **Testes de API:** [Requests](https://requests.readthedocs.io/)
- **Design Pattern:** Page Object Model (POM)
- **Gerenciamento de Ambiente:** Python-dotenv

## 🏗 Arquitetura e Padrões de Projeto

O framework utiliza o padrão **Page Object Model (POM)** para desacoplar a lógica de teste da representação técnica dos elementos da interface.

### Estrutura de Diretórios

- `/pages`: Contém as `Page Objects`, centralizando locators e interações de baixa abstração (ex: `base_page.py`, `login_page.py`).
- `/tests`: Scripts de teste de alto nível que validam regras de negócio e contratos de API.
- `conftest.py`: Configurações globais, fixtures de setup/teardown de browser e gerenciamento de sessões de autenticação.
- `.env`: Gestão de variáveis de ambiente e credenciais sensíveis (segurança em primeiro lugar).

## 🔍 Diferenciais Técnicos (Solução de Problemas)

Diferente de automações superficiais, este framework foi construído para lidar com desafios reais encontrados no projeto:

- **Testes de Contrato de API:** Validação rigorosa de payloads, tratando inconsistências entre documentação (Swagger) e implementação real (Sequelize/ORM).
- **Tratamento de Erros 500:** Scripts específicos para detectar e reportar vazamentos de stack trace e falhas de integridade de banco de dados (`ForeignKeyConstraintError`).
- **Resiliência:** Implementação de waits explícitos na `BasePage` para lidar com a latência de rede e renderização dinâmica de elementos.

## 🚀 Como Executar

1. Clone o repositório:

```bash
   git clone [https://github.com/seu-usuario/qa-automation-framework.git](https://github.com/seu-usuario/qa-automation-framework.git)

```

1. Instale as dependências:

```bash
pip install -r requirements.txt

```

1. Configure o arquivo `.env` com as credenciais necessárias.
2. Execute os testes:

```bash
pytest -v -s

```

---

**Autor:** David | SDET & QA Enthusiast
