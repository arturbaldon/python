# --------------------------------------------------------->
# PROBLEMA: "fatorial".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Digite o valor de N: "))

# calcular e exibir fatorial de N.
if 0 <= n <= 15:
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial = fatorial * i
    print(f"FATORIAL = {fatorial}")
