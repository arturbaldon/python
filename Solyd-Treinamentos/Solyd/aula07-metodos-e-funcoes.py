# criando uma função
def soma(n1, n2):
    resp = n1 + n2
    return resp

# chamando a função
resultado = soma(2, 3)
print(resultado)

print("-------------------------------------->")

def saudacao():
    print("Salve!")

saudacao()

i = 0
while i < resultado:
    saudacao()
    i += 1

print("-------------------------------------->")

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(tem_sete_itens("aaaaaaa"))
print(tem_sete_itens("aaaaaaaa"))
print(tem_sete_itens("aaaaaa"))

if tem_sete_itens("1234567"):
    print("Yeah!")
else:
    print("No!")

# da para passar praticamente qualquer coisa que tenha lengh. Um conjunto por exemplo
if tem_sete_itens({1, 2, 3, 4, 5, 6, 7}):
    print("ok, tem sete itens")
else:
    print("não tem sete itens")
