# --------------------------------------------------------->
# PROBLEMA: "notas".
# VER ARQUIVO: "04-estrutura-condicional-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# calcula e exibe a nota final.
nota_final = nota1 + nota2
print(f"NOTA FINAL = {nota_final:.1f}")

# verifica status reprovado.
if nota_final < 60.00:
    print("REPROVADO")
