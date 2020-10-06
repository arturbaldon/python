# --------------------------------------------------------->
# PROBLEMA: "soma_vetores".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos valores vai ter cada vetor? "))

lista_a = [0 for x in range(n)]
lista_b = [0 for x in range(n)]
lista_c = [0 for x in range(n)]

print("Digite os valores do vetor A:")
for i in range(0, n):
    lista_a[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(0, n):
    lista_b[i] = int(input())

# soma e exibe vetor resultante
print("VETOR RESULTANTE:")
for i in range(0, n):
    lista_c[i] = lista_a[i] + lista_b[i]
    print(lista_c[i])
