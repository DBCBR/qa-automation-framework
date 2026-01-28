import requests
import time
import re
import dotenv


class EmailHelper:
    def __init__(self):
        self.base_url = "https://mailsac.com/api"
        self.api_key = dotenv.get_key(".env", "mailsac-api-key")

    def gerar_email_temporario(self, prefixo="user_qa_david"):
        """
        Gera um e-mail único. O strip() e lower() garantem que 
        não existam espaços ou letras maiúsculas que confundam a API.
        """
        timestamp = int(time.time())
        email = f"{prefixo}_{timestamp}@mailsac.com"
        return email.strip().lower()

    def esperar_pelo_codigo(self, email):
        email = email.strip().lower()
        headers = {'Mailsac-Key': self.api_key}
        print(f"\n[DEBUG] Monitorando: https://mailsac.com/inbox/{email}")

        for i in range(25):
            try:
                response = requests.get(f"{self.base_url}/addresses/{email}/messages", headers=headers)
                if response.status_code == 200:
                    messages = response.json()
                    if isinstance(messages, list) and len(messages) > 0:
                        # Pegamos sempre a mensagem mais recente
                        msg_id = messages[0]['_id']
                        
                        # TENTATIVA 1: Ler como Texto Simples
                        res_text = requests.get(f"{self.base_url}/text/{email}/{msg_id}", headers=headers)
                        # TENTATIVA 2: Ler como HTML (Caso o texto falhe)
                        res_html = requests.get(f"{self.base_url}/body/{email}/{msg_id}", headers=headers)
                        
                        conteudo_total = res_text.text + res_html.text
                        
                        # Regex aprimorada para ignorar o que vem antes/depois
                        match = re.search(r'(\d{6})', conteudo_total)
                        
                        if match:
                            codigo = match.group(1)
                            print(f"[DEBUG] SUCESSO! Código {codigo} capturado.")
                            return codigo
                        else:
                            print(f"[DEBUG] E-mail chegou, mas código não achado no corpo. Conteúdo lido: {conteudo_total[:50]}...")
                    else:
                        print(f"[DEBUG] Tentativa {i+1}: Caixa vazia...")
                time.sleep(5)
            except Exception as e:
                print(f"[DEBUG] Erro: {e}")
                time.sleep(5)
        return None