# Tipo 1

lista = []

num = int(input("Número: "))
while (num != 0):
    lista.append(num)
    num = int(input("Número: "))

print(lista)

# substituir os valores 10 por 0
for i in range(len(lista)):
    if (lista[i] == 10):
        lista[i] = 0

print(lista)

# remover os valores 0 (zero)
while (0 in lista):
    lista.remove(0)

print(lista)