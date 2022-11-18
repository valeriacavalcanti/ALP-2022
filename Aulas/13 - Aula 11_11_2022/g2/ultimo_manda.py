numeros = []

while (True):
    numero = int(input())
    if (numero == 0):
        break
    numeros.append(numero)

ultimo = numeros[len(numeros) - 1]

for i in range(len(numeros) - 1):
    if (numeros[i] > ultimo):
        print(numeros[i])