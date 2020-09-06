# --------------------------------------------------------->
# PROBLEMA: "lanchonete".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
codigo = int(input("Código do produto comprado: "))
quantidade = int(input("Quantidade comprada: "))

# calcula e exibe o valor a pagar conforme o código.
if codigo == 1:
    valor_pagar = quantidade * 5.00
elif codigo == 2:
    valor_pagar = quantidade * 3.50
elif codigo == 3:
    valor_pagar = quantidade * 4.80
elif codigo == 4:
    valor_pagar = quantidade * 8.90
elif codigo == 5:
    valor_pagar = quantidade * 7.32
else:
    valor_pagar = 0

print(f"Valor a pagar: R$ {valor_pagar:.2f}")
