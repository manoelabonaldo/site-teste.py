import beautifulsoup4
import gspread
import oauth2client
import requests
import datetime
import pytz
import gdown
import os

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup

GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
GOOGLE_SHEETS_KEY = os.environ["GOOGLE_SHEETS_KEY"]
TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]
with open("credenciais.json", mode="w") as arquivo:
  arquivo.write(GOOGLE_SHEETS_CREDENTIALS)
conta = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json")
api = gspread.authorize(conta)
planilha = api.open_by_key(f'{GOOGLE_SHEETS_KEY}')
sheet = planilha.worksheet("Página1")


def puxa_listasuja(): 

  url = 'https://www.gov.br/trabalho-e-previdencia/pt-br/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/combate-ao-trabalho-escravo-e-analogo-ao-de-escravo'
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  links = soup.find_all('a')

  xlsx_links = []
  for link in soup.find_all("a"):
      href = link.get("href")
      if href and href.endswith(".xlsx") and "cadastro_de_empregadores" in href:
          xlsx_links.append(href)

  if xlsx_links:
      for link in xlsx_links:
          print(link)
  else:
      print("Não foi encontrado nenhum arquivo .xlsx files contendo a expressão 'cadastro_de_empregadores'.")
    
  lista_sujaatual = link

  range_name = 'A1:B1'

  timezone = 'America/Sao_Paulo'
  now = datetime.datetime.now(pytz.timezone(timezone)).strftime('%m/%d/%Y %H:%M:%S')
  service = build('sheets', 'v4', credentials=conta)
  values = [
      [link, now]
  ]
  request = service.spreadsheets().values().append(
      spreadsheetId=SPREADSHEET_ID,
      range=range_name,
      valueInputOption='USER_ENTERED',
      insertDataOption='INSERT_ROWS',
      body={'values': values}
  )
  response = request.execute()
  print('Informações adicionadas com sucesso.')
  Return "OK"
