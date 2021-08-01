equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input('Digite "S" para continuar: ').upper()

for i in range(len(equipamentos)):
    print(f"Equipamento..: {i+1}")
    print(f"Nome.........: {equipamentos[i]}")
    print(f"Valor........: {valores[i]}")
    print(f"Serial.......: {seriais[i]}")
    print(f"Departamento.: {departamentos[i]}")
    print()

busca = input("Digite o nome do equipamento que deseja buscar: ")
for i in range(len(equipamentos)):
    if busca == equipamentos[i]:
        print(f"Valor..: {valores[i]}")
        print(f"Serial.: {seriais[i]}")
        print()

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for i in range(len(equipamentos)):
    if depreciacao == equipamentos[i]:
        print(f"Valor antigo: {valores[i]}")
        valores[i] = valores[i] * 0.9
        print(f"Novo valor: {valores[i]}")
        print()

serial = int(input("Digite o serial do equipamento que será excluído: "))
for i in range(len(equipamentos)):
    if serial == seriais[i]:
        del equipamentos[i]
        del valores[i]
        del seriais[i]
        del departamentos[i]
        break

for i in range(len(equipamentos)):
    print(f"Equipamento..: {i+1}")
    print(f"Nome.........: {equipamentos[i]}")
    print(f"Valor........: {valores[i]}")
    print(f"Serial.......: {seriais[i]}")
    print(f"Departamento.: {departamentos[i]}")
    print()
