frase = input('Frase: ')
qtde = 0

for i in range(len(frase)):
    if (frase[i] >= 'A') and (frase[i] <= 'Z'):
        qtde += 1

print(qtde)
