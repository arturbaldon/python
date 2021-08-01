#----------------------------------------------------------------------------------------------------------------------#
# EXERCÍCIO: Crie um software de gerenciamento bancário. Esse software poderá ser capaz de criar clientes e contas.
# Cada cliente possui nome, cpf e idade. Cada conta possui um cliente, saldo, limite e sacar, depositar e consultar
# saldo.
#----------------------------------------------------------------------------------------------------------------------#

# importando classes
from cliente import Cliente
from conta import Conta

# criando objeto cliente
cliente1 = Cliente("Artur de Camargo Baldon", "02869821964", 39)

# exibindo cliente
print(cliente1)

# criando objeto conta
conta1 = Conta(cliente1.nome, 300, 1000)

# exibindo conta
print(conta1)

# saque
conta1.sacar(310)
print(conta1.saldo)

# deposito
conta1.depositar(30)
print(conta1.saldo)

# consulta
print(conta1.consulta())