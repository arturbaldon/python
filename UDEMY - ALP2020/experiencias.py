# --------------------------------------------------------->
# PROBLEMA: "experiencias".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
n = int(input("Quantos casos de teste serão digitados? "))

coelhos = 0
ratos = 0
sapos = 0

for i in range(n):
    quantidade_cobaias = int(input("Quantidade de cobaias: "))
    tipo_cobaia = input("Tipo de cobaia: ")
    if tipo_cobaia == 'c' or tipo_cobaia == 'C':
        coelhos = coelhos + quantidade_cobaias
    elif tipo_cobaia == 'r' or tipo_cobaia == 'R':
        ratos = ratos + quantidade_cobaias
    elif tipo_cobaia == 's' or tipo_cobaia == 'S':
        sapos = sapos + quantidade_cobaias

# calcula e exibe relatório final.
total_cobaias = coelhos + ratos + sapos
percentual_coelhos = (coelhos / total_cobaias) * 100
percentual_ratos = (ratos / total_cobaias) * 100
percentual_sapos = (sapos / total_cobaias) * 100

print()
print("RELATÓRIO FINAL:")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}")
print(f"Percentual de ratos: {percentual_ratos:.2f}")
print(f"Percentual de sapos: {percentual_sapos:.2f}")
