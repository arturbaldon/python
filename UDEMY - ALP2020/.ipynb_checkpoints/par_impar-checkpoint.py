# --------------------------------------------------------->
# PROBLEMA: "par_impar".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos números você vai digitar? "))

# verifica e exibe par/impar, positivo/negativo ou nulo.
for i in range(n):
    x = int(input("Digite um número: "))
    if x == 0:
        print("NULO")
    else:
        if x % 2 == 0:
            print("PAR", end=" ")
        else:
            print("IMPAR", end=" ")
        if x > 0:
            print("POSITIVO")
        else:
            print("NEGATIVO")
