# --------------------------------------------------------->
# PROBLEMA: "divisao".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos casos você vai digitar? "))

# entra com os valores e exibe a divisão.
for i in range(n):
    numerador = int(input("Entre com o numerador: "))
    denominador = int(input("Entre com o denominador: "))
    if denominador == 0:
        print("DIVISÃO IMPOSSÍVEL")
    else:
        divisao = numerador / denominador
        print(f"DIVISÃO = {divisao:.2f}")
