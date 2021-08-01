# --------------------------------------------------------->
# PROBLEMA: "baskara".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
valor01 = int(input("Primeiro valor: "))
valor02 = int(input("Segundo valor: "))
valor03 = int(input("Terceiro valor: "))

# verificar qual é o menor valor dentre os três.
if valor01 < valor02 and valor01 < valor03:
    menor = valor01
elif valor02 < valor03:
    menor = valor02
else:
    menor = valor03

print(f"MENOR = {menor}")
