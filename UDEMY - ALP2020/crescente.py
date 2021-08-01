# --------------------------------------------------------->
# PROBLEMA: "crescente".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite dois números:")
x = int(input())
y = int(input())

# verifica ordem crescente ou decrescente.
while x != y:
    if x < y:
        print("CRESCENTE!")
    else:
        print("DECRESCENTE!")
    print("Digite outros dois números:")
    x = int(input())
    y = int(input())
