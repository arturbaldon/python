#----------------------------------------------------------------------------------------------------------------------#
# Exercício: faça um formulário que pergunte o nome, cpf, endereço, idade, altura, e telefone. Imprima em um relatório
# organizado.
#----------------------------------------------------------------------------------------------------------------------#

# área de variáveis e entrada de dados
#
nome = input("Qual é o seu nome completo?\n")
cpf = input("Qual o seu CPF (somente os números)?\n")
endereco = input("Qual o seu endereço?\n")
idade = input("Qual é a sua idade?\n")
altura = input("Qual é a sua altura?\n")
telefone = input("Qual é o seu telefone (somente os números e com DDD)?\n")
telefone_formatado = "("+telefone[0:2]+")"+telefone[2:]

# área de processamento e saída de dados
#
print("NOME:", nome, "\tCPF:", cpf, "\nENDEREÇO:", endereco, "\nIDADE:", idade, "\tALTURA:", altura, "\tTELEFONE:", telefone_formatado)

