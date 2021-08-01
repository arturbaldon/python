# --------------------------------------------------------->
# PROBLEMA: "validacao_de_nota".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados e efetua validação.
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Valor inválido! Tente novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Valor inválido! Tente novamente: "))

# calcula e exime a média.
media = (nota1 + nota2) / 2
print(f"MEDIA = {media:.2f}")
