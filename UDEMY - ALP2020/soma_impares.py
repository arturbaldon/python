# --------------------------------------------------------->
# PROBLEMA: "soma_impares".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
print("Digite dois números:")
x = int(input())
y = int(input())

# ajusta em ordem crescente.
if x > y:
    troca = x
    x = y
    y = troca

# calcula e exibe soma dos impares.
soma = 0
for i in range(x+1, y):
    if i % 2 != 0:
        soma = soma + i

print(f"SOMA DOS IMPARES = {soma}")
