#----------------------------------------------------------------------------------------------------------------------#
# Exercício: faça um programa que pergunte a idade, peso e altura de uma pessoa e decide se ela está apta a ser do
# exército. Para entrar no exercito tem que ter mais de 18 anos, pesar mais ou igual de 60 kilos e medir mais ou igual
# 1.70 metros.
#----------------------------------------------------------------------------------------------------------------------#

print("QUESTIONÁRIO DE APTIDÃO PARA O EXÉRCITO\n---------------------------------------\n")
# área de variáveis e entrada de dados
#
idade = int(input("Qual é a sua idade?\n"))
peso = float(input("Qual é o seu peso?\n"))
altura = float(input("Qual é a sua altura?\n"))

# área de processamento e saída de dados
#
if (idade > 18) and (peso >= 60) and (altura >= 1.70):
    print("\nOK, VOCÊ ESTÁ APTO!\n")
else:
    print("\nNEGATIVO, VOCÊ NÃO ENTRA!\n")

print("------ FIM ------")