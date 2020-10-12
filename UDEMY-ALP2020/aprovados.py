# --------------------------------------------------------->
# PROBLEMA: "aprovados".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos alunos serão digitados? "))

lista_nome = [0 for x in range(n)]
lista_nota1 = [0 for x in range(n)]
lista_nota2 = [0 for x in range(n)]

for i in range(0, n):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
    lista_nome[i] = str(input())
    lista_nota1[i] = float(input())
    lista_nota2[i] = float(input())

# exibe alunos aprovados
print("Alunos aprovados:")

for i in range(0, n):
    media = (lista_nota1[i] + lista_nota2[i]) / 2.0
    if media >= 6.0:
        print(lista_nome[i])
