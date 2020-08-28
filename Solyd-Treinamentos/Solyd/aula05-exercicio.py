#----------------------------------------------------------------------------------------------------------------------#
# Exercício: faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa. Após isso o
# programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados. Após isso irá imprimir todos os
# nomes da lista.
#----------------------------------------------------------------------------------------------------------------------#

quantidade_pessoas = int(input("Quantas pessoas serão convidadas? "))
lista_convidados = []
contador = 1

for convidado in range(quantidade_pessoas):
    lista_convidados.append(input("Nome do convidado #" + str(contador) + ": "))
    contador += 1

for convidado in lista_convidados:
    print(convidado)
