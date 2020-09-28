# --------------------------------------------------------->
# PROBLEMA: "dentro_fora".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos números você vai digitar? "))

# verifica e conta dentro/fora do intervalo.
dentro = 0
fora = 0
for i in range(n):
    x = int(input("Digite um número: "))
    if 10 <= x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

# exibe contagem
print(f"{dentro} DENTRO")
print(f"{fora} FORA")
