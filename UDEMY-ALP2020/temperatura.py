# --------------------------------------------------------->
# PROBLEMA: "temperatura".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
escala = input("Você vai digitar a temperatura em qual escala (C/F)? ")

# usuário entra com a temperatura, calcula e exibe a
# temperatura equivalente.
if escala == 'f' or escala == 'F':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (5.0 / 9.0) * (fahrenheit - 32.0)
    print(f"Temperatura equivalente em Celsius: {celsius:.2f}")
elif escala == 'c' or escala == 'C':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * (9.0 / 5.0)) + 32.0
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")
else:
    print("Opção inválida")
