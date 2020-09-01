# --------------------------------------------------------->
# PROBLEMA: "dardo".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite as três distâncias:")
distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

# verifica maior distância:
if distancia1 > distancia2 and distancia1 > distancia3:
    maior = distancia1
elif distancia2 > distancia3:
    maior = distancia2
else:
    maior = distancia3

# exibe maior distância:
print(f"MAIOR DISTÂNCIA = {maior:.2f}")
