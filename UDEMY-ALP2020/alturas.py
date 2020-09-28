# --------------------------------------------------------->
# PROBLEMA: "alturas".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantas pessoas serão digitadas? "))

lista_nome = [0 for x in range(n)]
lista_idade = [0 for x in range(n)]
lista_altura = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa:")
    lista_nome[i] = input("Nome: ")
    lista_idade[i] = int(input("Idade: "))
    lista_altura[i] = float(input("Altura: "))

# calcula e exibe média
soma = 0
for i in range(0, n):
    soma = soma + lista_altura[i]

media = soma / n
print(f"\nAltura média: {media:.2f}")

# verifica e exibe percentual de menores 16 anos
menores = 0
for i in range(0, n):
    if lista_idade[i] < 16:
        menores = menores + 1

percentual = (menores * 100.0) / n
print(f"Pessoas com menos de 16 anos: {percentual:.1f}%")

# exibe nomes de menores de idade
for i in range(0, n):
    if lista_idade[i] < 16:
        print(lista_nome[i])
