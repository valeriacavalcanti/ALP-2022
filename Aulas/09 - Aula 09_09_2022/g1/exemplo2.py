# Tipo 2

lista = []
while (True):
    num = int(input("Número: "))
    if (num == 0):
        break
    lista.append(num)

print(lista)

# substituir os valores 10 por 0
for i in range(len(lista)):
    if (lista[i] == 10):
        lista[i] = 0

print(lista)