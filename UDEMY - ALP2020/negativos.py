# --------------------------------------------------------->
# PROBLEMA: "negativos".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos números você vai digitar? "))

lista = [0 for x in range(n)]
for i in range(0, n):
    lista[i] = int(input("Digite um número: "))

# verifica e exibe números negativos
print("NÚMEROS NEGATIVOS:")
for i in range(0, n):
    if lista[i] < 0:
        print(lista[i])
