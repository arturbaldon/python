# olha ai o booleano

var_verdadeiro = True
var_falso = False

print(type(var_verdadeiro), type(var_falso))

if var_verdadeiro == True:
    print("Var_verdadeiro é de fato, verdadeiro ora pois!")

# Comparações:
# == igual
# != diferente
# >, <, >= e <=
# and e or

a = input("valor de 'a': ") # por input, o tipo entra como string!!!
b = input("valor de 'b': ") # por input, o tipo entra como string!!!
c = input("valor de 'c': ") # por input, o tipo entra como string!!!

print(type(a), type(b), type(c)) # aqui vai sair string!

a = 2 # aqui fixo, entra como inteiro!
b = 1 # aqui fixo, entra como inteiro!
c = 9 # aqui fixo, entra como inteiro!

print(type(a), type(b), type(c)) # aqui vai sair inteiro!

if (a > b) and (c != 9):
    print("entrou no if!")
else:
    print("Entrou no else!")

if a > b:
    print(a, "é maior do que", b)
else:
    print(a, "não é maior do que", b)

if a > b and c != 9:
    print(a, "é maior do que", b)
else:
    print(a, "não é maior do que", b)

print(">----------------------------------------------------->\n")

print("Menu:\n1 => Fit\n2 => City\n3 => Civic\n")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("HONDA FIT")
elif opcao == "2":
    print("HONDA CITY")
elif opcao == "3":
    print("HONDA CIVIC")
else:
    print("Opção inválida seu bocó!")

print(">----------------------------------------------------->\n")

idade = 50

if not idade == 50:
    print("Você não tem 50 anos!")
else:
    print("Você tem 50 anos!")