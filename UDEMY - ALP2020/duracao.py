# --------------------------------------------------------->
# PROBLEMA: "duracao".
# VER ARQUIVO: "03-estrutura-sequencial-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
duracao = int(input("Digite a duração em segundos: "))

# extrai a hora, o resto, minuto e segundo.
hora = duracao // 3600
resto = duracao % 3600
minuto = resto // 60
segundo = resto % 60

# exibe a duração em formato hh:mm:ss.
print(f"{hora}:{minuto}:{segundo}")
