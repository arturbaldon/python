# --------------------------------------------------------->
# PROBLEMA: "pares_consecutivos".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
x = int(input("Digite um número inteiro: "))

# calcula a soma dos pares consecutivos.
while x != 0:
    if x % 2 != 0:
        x = x + 1
    soma = (x * 5) + 20
    print(f"SOMA = {soma}")
    x = int(input("Digite um número inteiro: "))
