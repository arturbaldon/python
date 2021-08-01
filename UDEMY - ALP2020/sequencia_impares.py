# --------------------------------------------------------->
# PROBLEMA: "sequencia_impares".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
x = int(input("Digite o valor de X: "))

# verifica e exibe os impares.
for i in range(x):
    if i % 2 != 0:
        print(i)
