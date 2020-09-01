# --------------------------------------------------------->
# PROBLEMA: "quadrante".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite os valores das coordenadas X e Y:")
x = int(input())
y = int(input())

# verifica o quadrante.
while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
    elif x < 0 and y > 0:
        print("QUADRANTE Q2")
    elif x < 0 and y < 0:
        print("QUADRANTE Q3")
    else:
        print("QUADRANTE Q4")
    print("Digite os valores das coordenadas X e Y:")
    x = int(input())
    y = int(input())
