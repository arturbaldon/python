# importando bibliotecas
import requests

texto = None

# realizar requisição:
try:
    requisicao = requests.get("https://putsreq.com/M5kvNYr7ePKunsXOI235")
    texto = requisicao.text
except Exception as erro:
    print("Erro na requisição:", erro)

print(texto)
