# --------------------------------------------------------->
# PROBLEMA: "medidas".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

# calcula área do quadrado, triangulo e trapézio.
area_quadrado = pow(a, 2)
area_triangulo = (a * b) / 2
area_trapezio = ((a + b) / 2) * c

# exibe área do trapezio, triangulo e trapézio.
print(f"ÁREA DO QUADRADO = {area_quadrado:.4f}")
print(f"ÁREA DO TRIANGULO = {area_triangulo:.4f}")
print(f"ÁREA DO TRAPÉZIO = {area_trapezio:.4f}")
