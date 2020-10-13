# --------------------------------------------------------->
# PROBLEMA: "soma_linhas".
# VER ARQUIVO: "07-matrizes-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

lista = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    print(f"Digite os elementos da {i+1}a. linha:")
    for j in range(0, n):
        lista[i][j] = float(input())

# gera lista com as somas dos elementos
lista_gerada = [0 for x in range(m)]

for i in range(0, m):
    soma = 0
    for j in range(0, n):
        soma = soma + lista[i][j]
    lista_gerada[i] = soma

# exibe lista gerada
print("VETOR GERADO:")
for i in range(0, m):
    print(f"{lista_gerada[i]:.1f}")
