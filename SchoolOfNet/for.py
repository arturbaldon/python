listNum = [2, 4, 6, 8, 10]
listName = ["artur", "ana"]

for item in listNum:
    print(item)

print("------------------------------------------------->")

for item in listNum[0:3]:
    print(item)

print("------------------------------------------------->")

for item in listNum[0:3]:
    if item > 2:
        print("maior que 2")

print("------------------------------------------------->")

for item in listName:
    print(item)

print("------------------------------------------------->")

for item in listName:
    if item == "ana":
        print(item)

print("------------------------------------------------->")

for item in listName:
    if not item == "ana":
        print(item)

