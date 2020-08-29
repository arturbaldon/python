# --------------------------------------------------------->
# PROBLEMA: "troco".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
preco_unitario = float(input("Preço unitário do produto: "))
quantidade_comprada = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

# calcula e exibe o valor do troco.
troco = dinheiro_recebido - (quantidade_comprada * preco_unitario)
print(f"TROCO = {troco:.2f}")
