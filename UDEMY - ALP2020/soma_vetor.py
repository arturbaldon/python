# --------------------------------------------------------->
# PROBLEMA: "soma_vetor".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
from typing import List

n = int(input("Quantos números você vai digitar? "))

lista = [0 for x in range(n)]
for i in range(0, n):
    lista[i] = float(input("Digite um número: "))

# exibe valores e calcula soma
soma = 0
print("\nVALORES = ", end="")
for i in range(0, n):
    print(f"{lista[i]:.1f}  ", end="")
    soma = soma + lista[i]

# exibe a soma e a média
print(f"\nSOMA = {soma:.2f}")
media = soma / n
print(f"MÉDIA = {media:.2f}")
