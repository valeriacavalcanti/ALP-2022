import random

numeros = []

while (len(numeros) < 6):
    novo = random.randint(1,60)
    if (novo not in numeros):
        numeros.append(novo)

numeros.sort()
print(numeros)