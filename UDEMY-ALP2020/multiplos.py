# --------------------------------------------------------->
# PROBLEMA: "multiplos".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite dois números inteiros:")
x = int(input())
y = int(input())

# verifica se são multiplos.
if x % y == 0 or y % x == 0:
    print("São multiplos")
else:
    print("Não são multiplos")
