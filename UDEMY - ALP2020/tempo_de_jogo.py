# --------------------------------------------------------->
# PROBLEMA: "tempo_de_jogo".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
hora_inicial = int(input("Hora inicial: "))
hora_final = int(input("Hora final: "))

# verifica e exibe a duração.
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
else:
    duracao = (24 - hora_inicial) + hora_final

print(f"O JOGO DUROU {duracao} HORA(S)")
