# --------------------------------------------------------->
# PROBLEMA: "consumo".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
distancia_percorrida = int(input("Distancia percorrida: "))
combustivel_gasto = float(input("Combustível gasto: "))

# calcula e exibe o consumo médio.
consumo_medio = distancia_percorrida / combustivel_gasto
print(f"Consumo medio = {consumo_medio:.3f}")
