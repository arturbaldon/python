# --------------------------------------------------------->
# PROBLEMA: "operadora".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
minutos = int(input("Digite a quantidade de minutos: "))

# calcular valor a ser pago.
if minutos <= 100:
    valor_pagar = 50.0
else:
    valor_pagar = 50.0 + ((minutos - 100.0) * 2.0)

# exibe valor a ser pago
print(f"Valor a pagar: R$ {valor_pagar:.2f}")
