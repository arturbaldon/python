# --------------------------------------------------------->
# PROBLEMA: "troco_verificado".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
preco_unitario = float(input("Preço unitário do produto: "))
quantidade_comprada = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

# calcula o total da compra e verifica se tem troco ou
# dinheiro insuficiente.
valor_compra = preco_unitario * quantidade_comprada

if dinheiro_recebido >= valor_compra:
    troco = dinheiro_recebido - valor_compra
    print(f"TROCO = {troco:.2f}")
else:
    falta_dinheiro = valor_compra - dinheiro_recebido
    print(f"DINHERO INSUFICIENTE. FALTAM {falta_dinheiro:.2f} REAIS")
