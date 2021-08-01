from datetime import datetime


def datahora(value):
    now = datetime.now()
    if value == "data_acesso":
        dia = now.day
        mes = now.month
        ano = now.year
        resposta = f"{dia}/{mes}/{ano}"
    elif value == "hora_acesso":
        hora = now.hour
        minuto = now.minute
        segundo = now.second
        resposta = f"{hora}:{minuto}:{segundo}"
    else:
        resposta = "ERRO FUNÇÃO DATAHORA"
    return resposta


def perguntar():
    print("O que deseja realizar?")
    print()
    print("<I> - Para Inserir um usuário")
    print("<P> - Para Pesquisar um usuário")
    print("<E> - Para Excluir um usuário")
    print("<L> - Para Listar um usuário")
    print("<S> - Para Sair")
    print()
    resposta = input("Opção: ").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [
        input("Digite o nome: ").upper(),
        input("Qual a última estação acessada: ").upper(),
        datahora("data_acesso"),
        datahora("hora_acesso")
    ]
    print()


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is None:
        print("Usuário não encontrado!")
    else:
        print("Nome..............: " + lista[0])
        print("Última estação....: " + lista[1])
        print("Data de acesso....: " + lista[2])
        print("Horário de acesso.: " + lista[3])
    print()


def excluir(dicionario, chave):
    if dicionario.get(chave) is None:
        print("Usuário não encontrado!")
    else:
        del dicionario[chave]
        print("Objeto eliminado!")
    print()


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
    print()
