# --------------------------------------------------------->
# PROBLEMA: "diagonal_negativos".
# VER ARQUIVO: "07-matrizes-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Qual a ordem da matriz? "))

lista = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        lista[i][j] = int(input(f"Elemento [{i},{j}]: "))

# verifica e exibe diagonal principal
print("DIAGONAL PRINCIPAL:")
for i in range(0, n):
    print(f"{lista[i][i]} ", end="")

# verifica e exibe quantidade de negativos
quantidade_negativos = 0
for i in range(0, n):
    for j in range(0, n):
        if lista[i][j] < 0:
            quantidade_negativos = quantidade_negativos + 1

print(f"\nQUANTIDADE DE NEGATIVOS = {quantidade_negativos}")
