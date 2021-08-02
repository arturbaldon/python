def perguntar():
    print("O que deseja realizar?")
    print()
    print("<I> - Para Inserir um usuário")
    print("<P> - Para Pesquisar um usuário")
    print("<E> - Para Excluir um usuário")
    print("<L> - Para Listar um usuário")
    print()
    resposta = input("Opção: ").upper()
    return resposta


def inserir(dicionario):
    chave = input("Digite o login: ").upper()
    dicionario[chave] = [
        input("Digite o nome: ").upper(),
        input("Digite a última data de acesso: "),
        input("Qual a última estação acessada: ").upper()
    ]
    print()


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is None:
        print("Usuário não encontrado!")
    else:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("ùltima estação.: " + lista[2])
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
