import os.path

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configurações da API do Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

ID_PLANILHA = "1yBNjXY1dj8gADpKUnwCYD094d0yDtcWRnFdDjA9uopM"
ABA = "Página1"

#função que faz a pesquisa no SEMrush e exporta os dados
def pesquisa (links):

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()

def main():
    creds = None
    # Verifica se o token existe
    if os.path.exists("token.json"):
        print("Token encontrado. Carregando credenciais...")
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        print("Token não encontrado. Iniciando fluxo de autenticação...")

    # Verifica se as credenciais são válidas ou se precisam ser atualizadas
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Credenciais expiradas. Atualizando...")
            creds.refresh(Request())
        else:
            try:
                print("Executando fluxo de autenticação do usuário...")
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                print(f"Erro durante o fluxo de autenticação: {e}")
                return

        # Salva as credenciais para a próxima execução
        with open("token.json", "w") as token:
            print("Salvando credenciais no arquivo token.json...")
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        # Chama a API do Sheets
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=ID_PLANILHA, range=ABA).execute()
        
        values = result.get("values", [])

        if not values:
            print('Planilha vazia')
            return
    
        print("Valores na planilha:")
        for row in values:
            links = [row[1]]

    except HttpError as err:
        print(f"Erro na chamada da API do Google Sheets: {err}")

if __name__ == "__main__":
    main()
