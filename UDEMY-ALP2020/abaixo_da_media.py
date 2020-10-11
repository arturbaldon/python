# --------------------------------------------------------->
# PROBLEMA: "abaixo_da_media".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos elementos vai ter o vetor? "))

lista = [0 for x in range(n)]

for i in range(0, n):
    lista[i] = float(input("Digite um número: "))

# calcula e exibe média do vetor
media = 0
for i in range(0, n):
    media = media + lista[i]

media = media / n
print(f"\nMÉDIA DO VETOR = {media:.3f}")

# verifica e exibe elementos abaixo da média
print("ELEMENTOS ABAIXO DA MÉDIA:")

for i in range(0, n):
    if lista[i] < media:
        print(f"{lista[i]:.1f}")
