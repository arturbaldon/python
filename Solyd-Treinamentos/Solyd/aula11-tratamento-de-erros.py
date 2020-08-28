import time

def abre_arquivo():
    try:
        arquivo = open("arquivo-doido.txt")
        return True
    except Exception as erro:
        print("Opa! Deu zica:", erro)
        return False

while not abre_arquivo():
    print("Tentando abrir o arquivo...")
    time.sleep(5)

print("Arquivo aberto com sucesso!")