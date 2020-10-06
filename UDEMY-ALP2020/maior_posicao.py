# --------------------------------------------------------->
# PROBLEMA: "maio_posicao".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos números você vai digitar? "))

lista = [0 for x in range(n)]
for i in range(0, n):
    lista[i] = float(input("Digite um número: "))

# verifica maior valor
maior_valor = lista[0]
posicao = 0
for i in range(1, n):
    if lista[i] > maior_valor:
        maior_valor = lista[i]
        posicao = i

# exibe maior valor e posição
print(f"\nMAIOR VALOR = {maior_valor:.1f}")
print(f"POSIÇÃO DO MAIOR VALOR = {posicao}")
