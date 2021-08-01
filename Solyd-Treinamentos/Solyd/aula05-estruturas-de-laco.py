carros = ["Etios", "Yaris", "Corola", "Hilux"]

for carro in carros:
    print(carro)

print("------------------------------------------>")

# função range
lista_de_numeros = range(5)
for n in lista_de_numeros:
    print(n)

print("------------------------------------------>")

lista_de_numeros2 = range(5, 10)
for n2 in lista_de_numeros2:
    print(n2)

print("------------------------------------------>")

lista_numeros_pares = range(0, 11, 2) # boa para pegar somente numeros pares, usa o recurso do step
for np in lista_numeros_pares:
    print(np)

print("------------------------------------------>")

# Na verdade não precisa criar a lista. Da pra fazer o for no range direto

for item in range(0, 10):
    print(item)

print("------------------------------------------>")

for i in range(4):
    print(carros[i])

print("------------------------------------------>")

for i in carros:
    print(i)

print("------------------------------------------>")

for i in range(len(carros)):
    print(carros[i])

print("------------------------------------------>")

palavra = "gabundo"
for letra in palavra:
    print(letra)

print("------------------------------------------>")

n = 0
while n < 10:
    print("O n ainda é menor do que 10, olha só:", n)
    n = n + 1

# para fazer iteração
i = i + 1 # jeito newba
i += 1 # jeito proplayer

print("------------------------------------------>")

lista_bandas = ["Slayer", "Iron Maiden", "Judas Priest", "Megadeth", "W.A.S.P."]

# supondo que não existisse a função lenght...
contador = 0
for banda in lista_bandas:
    contador += 1

print(contador)

print("------------------------------------------>")

# é, mas como tem a lenght....

print(len(lista_bandas))

print("------------------------------------------>")

n = 0
while True:
    print(n)
    if n == 20:
        break
    n += 1

print("------------------------------------------>")