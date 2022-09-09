import random

lista = []

while(len(lista) < 6):
    num = random.randint(1,60) # 1 2 3 4 5 6
    if (num not in lista):
        lista.append(num)

lista.sort()
print(lista)