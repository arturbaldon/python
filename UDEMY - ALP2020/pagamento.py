# --------------------------------------------------------->
# PROBLEMA: "pagamento".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))

# calcula e exibe o valor do pagamento e nome do funcionario.
pagamento = valor_hora * horas_trabalhadas
print(f"O pagamento para {nome} deve ser {pagamento:.2f}")
