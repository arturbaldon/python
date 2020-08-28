nome = "Artur"
idade = 39
altura = 1.77
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print(nome)
print(idade)
print(altura)
print(type(nome))
print(type(idade))
print(type(altura))

print(nome)
print(idade)
print(altura)
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)

print(">------------------------------->")

# Artur tem 39 anos e 1.77 de altura!
print(nome, "tem", idade, "anos e", altura, "de altura!")
print(nome + "tem" + str(idade) + "anos e" + str(altura) + "de altura!")
print(nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura!")

# Concatenando com o "+", pode armazenar tudo em uma variável
frase = nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura!"
print(frase)

print(">------------------------------->")

nome = input("Escreva seu nome: ")
idade = input("Escreva sua idade: ")
altura = input("Escreva sua altura: ")
print(nome, "tem", idade, "anos e", altura, "de altura!")

print(">------------------------------->")

numero1 = 27
numero2 = 53
resultado = numero1 + numero2

print(resultado)

# para tirar raiz quadrada, eleva o número a (1/2):
resultado = 25 ** (1/2)
print(resultado)
