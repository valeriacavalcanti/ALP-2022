lista = []

while (True):
    num = int(input("Número: "))
    if (num == 0):
        break
    lista.append(num)

print(lista)
print(num)

# substituir os valores 10 por zero
for i in range(len(lista)):
    if (lista[i] == 10):
        lista[i] = 0

print(lista)