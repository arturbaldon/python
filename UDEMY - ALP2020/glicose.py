# --------------------------------------------------------->
# PROBLEMA: "glicose".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
glicose = float(input("Digite a medida da glicose: "))

# verifica classificação.
if glicose <= 100:
    classificacao = "normal"
elif glicose <= 140:
    classificacao = "elevado"
else:
    classificacao = "diabetes"

# exibe a clasificação.
print(f"Classificação: {classificacao}")
