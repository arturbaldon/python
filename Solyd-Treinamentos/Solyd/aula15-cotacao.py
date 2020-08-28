# importando bibliotecas
import requests
import json
import time
import datetime

# esse entra em loop
while True:
    # efetuando requisição
    requisicao = requests.get("https://api.hgbrasil.com/finance")

    # capturando json
    cotacao = json.loads(requisicao.text)

    # formatando json
    name = cotacao["results"]["currencies"]["USD"]["name"]
    buy = cotacao["results"]["currencies"]["USD"]["buy"]
    sell = cotacao["results"]["currencies"]["USD"]["sell"]

    # imprime
    print("COTAÇÃO DO DIA")
    print(datetime.datetime.now())
    print("Moeda:", name, "\nValor de compra:", buy, "\nValor de venda:", sell)

    # aguarda o tempo para próxima requisição
    time.sleep(60)