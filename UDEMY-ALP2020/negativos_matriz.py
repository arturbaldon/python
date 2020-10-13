# --------------------------------------------------------->
# PROBLEMA: "negativos_matriz".
# VER ARQUIVO: "07-matrizes-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))

lista = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range(0, n):
        lista[i][j] = int(input(f"Elemento [{i},{j}]: "))

# verifica e exibe valores negativos
print("VALORES NEGATIVOS:")

for i in range(0, m):
    for j in range(0, n):
        if lista[i][j] < 0:
            print(lista[i][j])
