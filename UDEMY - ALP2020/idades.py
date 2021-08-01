# --------------------------------------------------------->
# PROBLEMA: "idades".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Dados da primeira pessoa:")
nome_pessoa1 = input("Nome: ")
idade_pessoa1 = int(input("Idade: "))

print("Dados da segunda pessoa:")
nome_pessoa2 = input("Nome: ")
idade_pessoa2 = int(input("Idade: "))

# calcula idade média entre as duas pessoas.
idade_media = (idade_pessoa1 + idade_pessoa2) / 2

# exibe os nomes e idade média
print(f"A idade média de {nome_pessoa1} e {nome_pessoa2} é de {idade_media:.1f} anos")
