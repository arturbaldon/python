arquivo = open("arquivo.txt", "w")
arquivo.write("Trabalhando com arquivos no Python!\n\n")

for i in range(1, 11):
    arquivo.write(str(i) + "\n")

arquivo = open("arquivo.txt", "r")
print(arquivo.read())

arquivo = open("arquivo.txt", "r")
for linha in arquivo:
    print(linha)
