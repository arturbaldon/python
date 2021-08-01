# --------------------------------------------------------->
# PROBLEMA: "baskara".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# biblioteca para funções matemáticas.
import math

# usuário entra com os dados solicitados.
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

# calcula o valor de delta.
delta = pow(b, 2.0) - (4 * a * c)

# verifica se a equação possui raízes reais e caso positivo
# calcular e exibir os valores de x1 e x2.
if delta < 0:
    print("Esta equação não possui raízes reais.")
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")
