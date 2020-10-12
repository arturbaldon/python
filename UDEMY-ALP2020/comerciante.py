# --------------------------------------------------------->
# PROBLEMA: "comerciante".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Serão digitados dados de quantos produtos? "))

lista_nome = [0 for x in range(n)]
lista_preco_compra = [0 for x in range(n)]
lista_preco_venda = [0 for x in range(n)]

for i in range(0, n):
    print(f"Produto {i+1}:")
    lista_nome[i] = str(input("Nome: "))
    lista_preco_compra[i] = float(input("Preço de compra: "))
    lista_preco_venda[i] = float(input("Preço de venda: "))

# calcula e exibe relatorio
print("\nRELATÓRIO:")

lucro_abaixo_10 = 0
lucro_entre_10_20 = 0
lucro_acima_20 = 0

for i in range(0, n):
    lucro = lista_preco_venda[i] - lista_preco_compra[i]
    lucro_percentual = (lucro * 100) / lista_preco_compra[i]
    if lucro_percentual < 10:
        lucro_abaixo_10 = lucro_abaixo_10 + 1
    elif lucro_percentual <= 20:
        lucro_entre_10_20 = lucro_entre_10_20 + 1
    else:
        lucro_acima_20 = lucro_acima_20 + 1

print(f"Lucro abaixo de 10%: {lucro_abaixo_10}")
print(f"Lucro entre 10% e 20%: {lucro_entre_10_20}")
print(f"Lucro acima de 20%: {lucro_acima_20}")

total_compra = 0
total_venda = 0
for i in range(0, n):
    total_compra = total_compra + lista_preco_compra[i]
    total_venda = total_venda + lista_preco_venda[i]

lucro_total = total_venda - total_compra

print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
