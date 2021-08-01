# --------------------------------------------------------->
# PROBLEMA: "aumento".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
salario = float(input("Digite o salário da pessoa: "))

# verifica a porcentagem.
if salario <= 1000.0:
    porcentagem = 20
elif salario <= 3000.0:
    porcentagem = 15
elif salario <= 8000.0:
    porcentagem = 10
else:
    porcentagem = 5

# calcula o aumento e o novo salário.
aumento = (salario * porcentagem) / 100
novo_salario = salario + aumento

# exibe novo salário, o aumento e a porcentagem.
print(f"Novo salário = R$ {novo_salario:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")
