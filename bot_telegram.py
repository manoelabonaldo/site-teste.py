import os 

import json
import requests


GOOGLE_SHEETS_CREDENTIALS = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
TELEGRAM_ADMIN_ID = os.environ["TELEGRAM_ADMIN_ID"]


def bot_dotelegram(): 
   
  update_id = update['update_id']
  first_name = update['message']['from']['first_name']
  last_name = update['message']['from']['last_name']
  user_name = update['message']['from']['username']
  sender_id = update['message']['from']['id']
  date = datetime.fromtimestamp(update['message']['date']).date()
  time = datetime.fromtimestamp(update['message']['date']).time()
  chat_id = update['message']['chat']['id']
  
  try:
      message = update['message']['text']
  except KeyError:
      print("received unhandled message type")
      message=''
  #return chat_id, texto
  
  if "username" in update["message"]["from"]:
    username = f' @{update["message"]["from"]["username"]}'
  else:
    username = ""
      
  if request.method == 'POST':
     update = request.get_json()

  if message == "oi":
     texto_resposta = f"Olá. 🤖\n\nSou a Antonieta, uma robô que analisa e registra a lista suja do trabalho escravo.\n\nO que você deseja saber em relação à lista suja mais atual?\n\nDigite 1️⃣ para descobrir o número total de trabalhadores que constam na lista suja do trabalho escravo.\nDigite 2️⃣ para saber em quais atividades econômicas o trabalho análogo à escravidão é mais frequente.\nDigite 3️⃣ para descobrir qual foi o estado em que mais pessoas foram resgatadas.\nDigite 4️⃣ para denunciar casos de trabalho análogo à escravidão.\nDigite 5️⃣ para maiores informações sobre trabalho escravo e outras dúvidas. \n\n📊🔍Os dados analisados aqui são fornecidos pelo Ministério do Trabalho e Previdência do Brasil por meio do Cadastro de Empregadores que tenham submetido trabalhadores a condições análogas à de escravo (Lista Suja do Trabalho Escravo)."
  elif message == "1":
     texto_resposta = f"Infelizmente o trabalho análogo ao de escravo ainda é uma realidade no Brasil.\n\nNa lista suja mais atual, {int(Soma_Trabalhadores)} trabalhadores foram resgatados em condições análogas à escravidão."
  elif message == "2":
     texto_resposta = f"As atividades econômicas com maior frequência de trabalho escravo na lista suja mais atual são, respectivamente:\n\n{b['CNAE'].loc[0]}, \n{b['CNAE'].loc[1]}, \ne { b['CNAE'].loc[2]}."
  elif message == "3":
     texto_resposta = f"O estado com o maior número de trabalhadores em situação análoga a escravidão é {Trabalhadores_UF['UF'].loc[0]}, com um total de {int(Trabalhadores_UF['Trabalhadores envolvidos'].loc[0])} trabalhadores resgatados. \n\nEsse valor é referente à lista suja mais atual."
  elif message == "4":
     texto_resposta = f"O Ministério do Trabalho usa a plataforma IPÊ para coletar denúncias 🚨 de trabalho análogo à escravidão. O sigilo da denúncia é garantido e você pode realizá-la clicando no link a seguir. https://ipe.sit.trabalho.gov.br/#!/"
  elif message == "5":
     texto_resposta = f"A maioria dos trabalhadores que formam a mão de obra escrava é migrante, de baixa renda, oriunda de regiões marcadas pela fome e pobreza, onde há pouca oportunidade de sustento. \n\nLonge das estruturas de proteção social, eles são facilmente envolvidos por relações de trabalho violentas e têm sua força de trabalho extraída ao máximo. \n\nMuitos acabam sendo explorados e expostos a condições de trabalho degradantes, sem acesso à água potável, banheiro, comida de qualidade, sem um teto digno, vivendo sob ameaças e sem pagamento.\n\n⚖️ O Art. 149. do CP afirma ser crime reduzir alguém a condição análoga à de escravo quando há:  \n\n- Trabalho forçado; \n- Condições degradantes de trabalho; \n- Restrição de locomoção; \n- Servidão por dívida.  \n\nConsidera-se trabalho escravo quando alguma das situações é observada.\n\n📂 Para acessar a Lista Suja do Trabalho Escravo, acesse o link abaixo. www.gov.br/trabalho-e-previdencia/pt-br/pt-br/composicao/orgaos-especificos/secretaria-de-trabalho/inspecao/areas-de-atuacao/combate-ao-trabalho-escravo-e-analogo-ao-de-escravo\n\n\n🤖 O robô do trabalho escravo foi desenvolvido por Manoela Bonaldo (📩 bonaldomanoela@gmail.com) para a disciplina de Algoritmos de Automação, dos professores Álvaro Justen e Guilherme Felitti, no Master em Jornalismo de Dados, Automação e Datastorytelling, no Insper.\n\n"
  else:
     texto_resposta = f"Olá. 🤖\n\nSou a Antonieta, uma robô que analisa e registra a lista suja do trabalho escravo.\n\nO que você deseja saber em relação à lista suja mais atual?\n\nDigite 1️⃣ para descobrir o número total de trabalhadores que constam na lista suja do trabalho escravo.\nDigite 2️⃣ para saber em quais atividades econômicas o trabalho análogo à escravidão é mais frequente.\nDigite 3️⃣ para descobrir qual foi o estado em que mais pessoas foram resgatadas.\nDigite 4️⃣ para denunciar casos de trabalho análogo à escravidão.\nDigite 5️⃣ para maiores informações sobre trabalho escravo e outras dúvidas. \n\n📊🔍Os dados analisados aqui são fornecidos pelo Ministério do Trabalho e Previdência do Brasil por meio do Cadastro de Empregadores que tenham submetido trabalhadores a condições análogas à de escravo (Lista Suja do Trabalho Escravo)."

  nova_mensagem = {"chat_id": chat_id, "text": texto_resposta}
  resposta = requests.post(f"https://api.telegram.org./bot{TELEGRAM_API_KEY}/sendMessage", data = nova_mensagem)
