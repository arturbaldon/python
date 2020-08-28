# importando biblioteca externa
import sys

# passado por linha de comando:
# * argumento 0 é o nome do programa.
# * argumento 1 é o método
# * argumento 2 é o n1
# * argumento 3 é o n2
argumentos = sys.argv

# função para somar dois números
def soma(n1, n2):
    return n1 + n2

# função para subtrair dois números
def subt(n1, n2):
    return n1 - n2

# processamento, chamada das funções
if argumentos[1] == "soma":
    resposta = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "subt":
    resposta = subt(float(argumentos[2]), float(argumentos[3]))
else:
    resposta = "parâmetro inválido"

print(resposta)

# agora para executar, vai no cmd (terminal) e estando no diretório do programa, chama o python e passa os
# argumentos, onde:
# arg0 é o nome do programa (o nome do arquivo .py)
# arg1 é o método (soma ou subt)
# arg2 e arg3, os n1 e n2 respectivamente