# --------------------------------------------------------->
# PROBLEMA: "combustivel".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# inicializa variavel de contagem, usuário entra com os
# dados solicitados e inicia a contagem.
codigo = 0
alcool = 0
gasolina = 0
diesel = 0
while codigo != 4:
    codigo = int(input("Informe um código (1, 2, 3) ou 4 para parar: "))
    if codigo == 1:
        alcool = alcool + 1
    elif codigo == 2:
        gasolina = gasolina + 1
    elif codigo == 3:
        diesel = diesel + 1

# exibe contagem dos dados
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
