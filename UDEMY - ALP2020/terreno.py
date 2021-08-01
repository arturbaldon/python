# --------------------------------------------------------->
# PROBLEMA: "terreno".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor_metro_quadrado = float(input("Digite o valor do metro quadrado: "))

# calcula e exibe área do terreno.
area_terreno = largura * comprimento
print(f"Área do terreno = {area_terreno:.2f}")

# calcula e exibe preço do terreno.
preco_terreno = valor_metro_quadrado * area_terreno
print(f"Preço do terreno = {preco_terreno:.2f}")
