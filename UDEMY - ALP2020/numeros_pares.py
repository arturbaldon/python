# --------------------------------------------------------->
# PROBLEMA: "numeros_pares".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos números você vai digitar? "))

lista = [0 for x in range(n)]
for i in range(0, n):
    lista[i] = int(input("Digite um número: "))

# verifica e exibe numeros pares
print("\nNÚMEROS PARES:")
quantidade_pares = 0
for i in range(0, n):
    if lista[i] % 2 == 0:
        print(f"{lista[i]}  ", end="")
        quantidade_pares = quantidade_pares + 1

print(f"\n\nQUANTIDADE DE PARES = {quantidade_pares}")
