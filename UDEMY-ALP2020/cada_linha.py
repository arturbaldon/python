# --------------------------------------------------------->
# PROBLEMA: "cada_linha".
# VER ARQUIVO: "07-matrizes-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Qual a ordem da matriz? "))

lista = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        lista[i][j] = int(input(f"Elemento [{i},{j}]: "))

# verifica e exibe maior elemento de cada linha
print("MAIOR ELEMENTO DE CADA LINHA:")


for i in range(0, n):
    maior_elemento = lista[i][0]
    for j in range(0, n):
        if lista[i][j] > maior_elemento:
            maior_elemento = lista[i][j]
    print(maior_elemento)
