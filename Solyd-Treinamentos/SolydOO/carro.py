# Herança. Importanto a classe "pai"
from veiculo import Veiculo

# criando a classe
class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: tanque cheio")
        else:
            self.tanque += litros