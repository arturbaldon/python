# importando a classe
from veiculo import Veiculo
from carro import Carro

# criando o objeto, uma instância
caminhao_rosa = Veiculo("rosa", 6, "Volvo", 10)

print(caminhao_rosa)
print(type(caminhao_rosa))
print(caminhao_rosa.cor)
print(caminhao_rosa.rodas)
print(caminhao_rosa.marca)
print(caminhao_rosa.tanque)

print("CAMINHÃO ROSA ---------------------------------------------------------->")
print("Cor:", caminhao_rosa.cor, "\nMarca:", caminhao_rosa.marca, "\nTanque:", caminhao_rosa.tanque)

# criando o objeto, uma instância
carro_azul = Carro("azul", "BMW", 30)

print("CARRO AZUL ------------------------------------------------------------->")
print("Cor:", carro_azul.cor, "\nRoda:", carro_azul.rodas, "\nMarca:", carro_azul.marca, "\nTanque:", carro_azul.tanque)

# abastece o carro...
carro_azul.abastecer(10)
print(carro_azul.tanque)

carro_azul.abastecer(25)
print(carro_azul.tanque)

# abastece mais o caminhão...
caminhao_rosa.abastecer(100)
print(caminhao_rosa.tanque)
