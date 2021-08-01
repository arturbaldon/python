# --------------------------------------------------------->
# PROBLEMA: "media_pares".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos elementos vai ter o vetor? "))

lista = [0 for x in range(n)]
media = 0
divisor = 0

for i in range(0, n):
    lista[i] = int(input("Digite um número: "))
    if lista[i] % 2 == 0:
        media = media + lista[i]
        divisor = divisor + 1

# exibe media dos pares se ouver
if media != 0:
    media = media / divisor
    print(f"MÉDIA DOS PARES = {media:.1f}")
else:
    print("NENHUM NÚMERO PAR")
