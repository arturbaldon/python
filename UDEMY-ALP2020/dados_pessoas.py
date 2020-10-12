# --------------------------------------------------------->
# PROBLEMA: "dados_pessoas".
# VER ARQUIVO: "06-vetores-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantas pessoas serão digitadas? "))

lista_altura = [0 for x in range(n)]
lista_genero = [0 for x in range(n)]

for i in range(0, n):
    lista_altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    lista_genero[i] = (input(f"Genero da {i+1}a pessoa: "))

# verifica e exibe menor e maior altura, media de altura das
# mulheres e numero de homens
menor_altura = lista_altura[0]
maior_altura = lista_altura[0]
media_altura_mulheres = 0
conta_mulheres = 0
conta_homens = 0
for i in range(1, n):
    if lista_altura[i] < menor_altura:
        menor_altura = lista_altura[i]
    if lista_altura[i] > maior_altura:
        maior_altura = lista_altura[i]
    if lista_genero[i] == 'f' or lista_genero[i] == 'F':
        media_altura_mulheres = media_altura_mulheres + lista_altura[i]
        conta_mulheres = conta_mulheres + 1
    elif lista_genero[i] == 'm' or lista_genero[i] == 'M':
        conta_homens = conta_homens + 1

print(f"Menor altura = {menor_altura:.2f}")
print(f"Maior altura = {maior_altura:.2f}")

media_altura_mulheres = media_altura_mulheres / conta_mulheres
print(f"Media das alturas das mulheres = {media_altura_mulheres:.2f}")

print(f"Numero de homens = {conta_homens}")
