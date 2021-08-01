import requests
import json

cidade = input("Escreva a sua cidade: ")

requisicao = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=8e138e6d2b7f251c43fbf64645cd2900")

tempo = json.loads(requisicao.text)

print("Condição do tempo:", tempo["weather"][0]["main"])
print("Temperatura:", float(tempo["main"]["temp"]) - 273.15)