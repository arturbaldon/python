# --------------------------------------------------------->
# PROBLEMA: "media_idades".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite as idades:")
idade = int(input())

# ler numero indeterminado de idades e calcular a media.
if idade < 0:
    print("IMPOSSÍVEL CALCULAR")
else:
    divisor = 0
    media = 0
    while idade >= 0:
        divisor = divisor + 1
        media = media + idade
        idade = int(input())
    media = media / divisor
    print(f"MEDIA = {media:.2f}")
