# --------------------------------------------------------->
# PROBLEMA: "senha_fixa".
# VER ARQUIVO: "05-estruturas-repetitivas-exercicios".
# --------------------------------------------------------->

# usuário entra com os dados solicitados.
senha_digitada = int(input("Digite a senha: "))

# verifica a senha.
while senha_digitada != 2002:
    senha_digitada = int(input("Senha Inválida! Tente novamente: "))

# acesso concedido.
print("Acesso permitido!")
