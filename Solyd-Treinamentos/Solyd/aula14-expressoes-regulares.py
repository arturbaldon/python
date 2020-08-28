# importando bibliotecas
import re
import requests

requisicao = requests.get("https://www.kaldicafe.com.br/site/#contato")
#---------------------------------------------------------------------------------------------------------------------->

string1 = "o gato é bonito"

# "r" é RAW string
# o "." equivale a qualquer caractere
# tem também o "\w" que equivale a qualquer caractere menos espaço em branco
padrao = re.search(r"gat.", string1)

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado")

#---------------------------------------------------------------------------------------------------------------------->

string2 = "o gato, a gata, os gatinhos e os gatões"

# o "+" repete indefinidamente até o fim da palavra
padrao = re.findall(r"gat\w+", string2)

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")

#---------------------------------------------------------------------------------------------------------------------->

string3 = "arturbaldon@gmail.com"

padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", string3)

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")

#---------------------------------------------------------------------------------------------------------------------->

padrao = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", requisicao.text)

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado")