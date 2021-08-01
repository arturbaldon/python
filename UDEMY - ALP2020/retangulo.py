# --------------------------------------------------------->
# PROBLEMA: "retangulo".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# biblioteca para funções matemática.
import math

# usuário entra com os dados solicitados.
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

# calcula área, perimetro e diagonal do retangulo.
area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = math.sqrt(pow(base, 2) + pow(altura, 2))

# exibe área, perímetro e diagonal do retangulo.
print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
