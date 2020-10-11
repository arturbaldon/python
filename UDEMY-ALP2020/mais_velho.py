# --------------------------------------------------------->
# PROBLEMA: "mais_velho".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantas pessoas você vai digitar? "))

lista_nome = [0 for x in range(n)]
lista_idade = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa:")
    lista_nome[i] = input("Nome: ")
    lista_idade[i] = int(input("Idade: "))

# verifica pessoa mais velha
maior_idade = lista_idade[0]
posicao = 0
for i in range(1, n):
    if lista_idade[i] > maior_idade:
        maior_idade = lista_idade[i]
        posicao = i

print(f"PESSOA MAIS VELHA = {lista_nome[posicao]}")
