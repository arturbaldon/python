# importando requisições
import requests
import json

# função para requisição e extrair o JSON para um dicionário Python
def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo + "&r=&apikey=c9d4370e")
        dicionario = json.loads(req.text)
        return dicionario
    except Exception as erro:
        print("Erro:", erro)
        return None

# função para exibir resultado
def printar_detalhes(filme):
    print("Título:", filme["Title"])
    print("Diretor:", filme["Director"])
    print("Atores:", filme["Actors"])
    print("Ano:", filme["Year"])
    print("Gênero:", filme["Genre"])
    print(" ")

# menu e entrada de dados
sair = False
while not sair:
    opcao = input("Escreva o nome do filme para consultar, ou SAIR para fechar o programa...\nR: ")
    if opcao == "SAIR":
        sair = True
    else:
        filme = requisicao(opcao)
        if filme["Response"] == "False":
            print("Filme não encontrado")
        else:
            printar_detalhes(filme)