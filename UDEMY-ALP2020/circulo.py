# --------------------------------------------------------->
# PROBLEMA: "circulo".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# biblioteca para funções matemáticas.
import math

# usuário entra com os dados solicitados.
raio = float(input("Digite o valor do raio do circulo: "))

# calcula e exibe a área do círculo.
area = math.pi * pow(raio, 2)
print(f"AREA = {area:.3f}")
