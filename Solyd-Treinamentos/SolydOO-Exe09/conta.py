class Conta:

    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = 0 - limite

    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Erro no depósito")

    def consulta(self):
        return self.saldo

    def __str__(self):
        return "Cliente: " + str(self.cliente) + "\nSaldo: " + str(self.saldo) + "\nLimite: " + str(self.limite)