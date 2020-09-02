# --------------------------------------------------------->
# PROBLEMA: "media_ponderada".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos casos você vai digitar? "))

# entrar com os três valores e exibe a média ponderada.
for i in range(n):
    print("Digite três números:")
    x1 = float(input())
    x2 = float(input())
    x3 = float(input())
    media_ponderada = ((x1 * 2) + (x2 * 3) + (x3 * 5)) / 10
    print(f"MEDIA = {media_ponderada:.1f}")
