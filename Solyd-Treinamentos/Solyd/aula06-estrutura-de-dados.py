# isso é uma lista (list). No caso, a lista é dinâmica, é mutável. Pode adicionar e remover itens.
list_carros = ["Etios", "Fit", "Yaris", "Corola", "Hylux"]

# isso é uma tupla (tuple). No caso, a tupla não é mutável. Possui sempre os mesmos itens.
tuple_carros = ("Etios", "Fit", "Yaris", "Corola", "Hylux")

# isso é um dicionário. No caso, possui chave e valor
dict_carros = {"Etios":"Branco", "Fit":"Azul", "Yaris":"Vermelho", "Corola":"Preto", "Hylux":"Prata"}

# isso é um conjunto. No caso, só tem o valor, diferente do dicionario que tem chave : valor. No conjunto, não há itens
# repetidos, como numa lista. O conjunto não é ordenado.
set_carros = {"Etios", "Fit", "Yaris", "Corola", "Hylux"}

#----------------------------------------------------------------------------------------------------------------------#

print(tuple_carros)
print(type(tuple_carros))
print(tuple_carros[1])
for carro in tuple_carros:
    print(carro)

if "Corola" in tuple_carros:
    print("Tem o item na tupla")
else:
    print("Não tem o item na tupla")

print("---------------------------------------------->")

print(dict_carros)
print(type(dict_carros))

for carro in dict_carros:
    print(carro)

print(dict_carros["Hylux"])

if "Vermelho" in dict_carros.values():
    print("Tem vermelho no dicionario")
else:
    print("Não tem ver")

print("---------------------------------------------->")

for chaves in dict_carros.keys():
    print(chaves)

print("---------------------------------------------->")

for valores in dict_carros.values():
    print(valores)

print("---------------------------------------------->")

dict_carros["Fit"] = "Cinza"
print(dict_carros["Fit"])

print("---------------------------------------------->")

dict_carros["Rav-4"] = "Dourado"
print(dict_carros)

print("---------------------------------------------->")

set_carros.add("Rav-4")
print(set_carros)

print("---------------------------------------------->")

# inicializar estrutura vazia

lista_exemplo = []
tupla_exemplo = ()
dicionario_exemplo = {}
conjunto_exemplo = set()

print(type(lista_exemplo), type(tupla_exemplo), type(dicionario_exemplo), type(conjunto_exemplo))