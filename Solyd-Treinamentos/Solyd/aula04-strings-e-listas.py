frase = "Oi, tudo bem?"
lista_nomes = ["João", "Maria", "Guilherme", "Diego"]

print(type(frase), type(lista_nomes))
print(lista_nomes)
print(lista_nomes[0], lista_nomes[1], lista_nomes[2], lista_nomes[3])
print(lista_nomes[0])
print(lista_nomes[1])
print(lista_nomes[2])
print(lista_nomes[3])
print(frase[0:10])
print(frase[5:10])
print(frase[0:13:1]) # o terceiro índice indica quantos passo ele vai pegar. O padrão é esse, de 1 em 1.
print(frase[0:13:2]) # Aqui vai pular 1
print(lista_nomes[0:2])
print(lista_nomes[-1]) # Aqui inverte a ordem. Muito bom para pegar o ultimo item da lista.
print(frase[::-1])

# use o método append para adicionar item na lista
lista_nomes.append("Ana")
print(lista_nomes)
print(lista_nomes[4])

# use o método remove para remover item na lista
lista_nomes.remove("Diego")
print(lista_nomes)

# use o método clear para limpar a lista
lista_nomes.clear()
print(lista_nomes)

# use o método insert com posição para incluir item
lista_nomes = ["João", "Maria", "Guilherme", "Diego"]
lista_nomes.insert(1, "Artur")
print(lista_nomes)

# conta quantos tem do mesmo item na lista
lista_nomes.append("Maria")
print(lista_nomes)
contador = lista_nomes.count("Maria")
print("Tem quantas Marias?... ", contador)

# tamanho
print(len(frase)) #retorna o tamanho da frase, a quantidade de caracteres
print(len(lista_nomes)) #retorna quantos itens há na lista

# o método pop imprime e remove o ultimo item da lista
print(lista_nomes.pop())
print(lista_nomes)

# deixa tudo em minusculo
palavraum = "CASA DO CARALHO"
print(palavraum)
print(palavraum.lower())

# usa o split para quebrar a frase, e com isso a string passa a ser uma lista
palavraum_separado = palavraum.split(" ")
print(palavraum_separado)

# concatena
palavraum_novo = "vai pra " + palavraum
print(palavraum_novo)

# deixa tudo em minusculo
palavraum_novo = palavraum_novo.upper()
print(palavraum_novo)
