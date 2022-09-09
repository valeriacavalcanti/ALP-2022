lista = []

num = int(input("Número: "))
while (num != 0):
    lista.append(num)
    num = int(input("Número: "))


print(lista)
print(num)

# substituir os valores 10 por zero
for i in range(len(lista)):
    if (lista[i] == 10):
        lista[i] = 0

print(lista)

# remover o valor zero da lista
while (0 in lista):
    lista.remove(0)

print(lista)

# exibir o índice do valor 30 na lista
if (30 in lista):
    for i in range(len(lista)):
        if (lista[i] == 30):
            print(i)
            break

if (30 in lista):
    print(lista.index(30))

# ordenar a lista
lista.sort()

print(lista)