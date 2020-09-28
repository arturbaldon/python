# --------------------------------------------------------->
# PROBLEMA: "tabuada".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Deseja a tabuada para qual valor? "))

# calcula e exibe a tabuada.
for i in range(1, 11):
    produto = n * i
    print(f"{n} x {i} = {produto}")
