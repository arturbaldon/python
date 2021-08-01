#----------------------------------------------------------------------------------------------------------------------#
# Exercício: Escreva uma função que recebe um objeto de coleção e retorna o valor de maior numero dentro da coleção.
# Faça outra função que retorna o menor numero desta coleção.
#----------------------------------------------------------------------------------------------------------------------#

# variáveis e coleções
tuple_colecao = (43, 57, 33, 48, 31, 34)

# função para retornar o item de maior valor
def valor_maior(colecao):
    x = colecao[0]
    for item in colecao:
        if item > x:
            x = item
    return x

# função para retornar o item de menor valor
def valor_menor(colecao):
    x = colecao[0]
    for item in colecao:
        if item < x:
            x = item
    return x

# chama função de valor maior e imprime
print("O maior valor da coleção é " + str(valor_maior(tuple_colecao)))

# chama função de valor menor e imprime
print("O menor valor da coleção é " + str(valor_menor(tuple_colecao)))

# agora, faz a versão PRO! Utilizando as funções build-in do Python
print("\nVERSÃO PROFISSIONAL:\n")

# função MAX
print("O maior valor da coleção é " + str(max(tuple_colecao)))

# função MIN
print("O menor valor da coleção é " + str(min(tuple_colecao)))
