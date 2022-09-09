binario = ""

while True:
    b = int(input("Digito: "))
    if (b != 0) and (b != 1):
        break
    binario += str(b)

print(binario)
