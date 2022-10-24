numeros = []
maisculos = []
minusculos = []
especiais = []

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= '0') and (frase[i] <= '9'):
        numeros.append(frase[i])
    elif (frase[i] >= 'A') and (frase[i] <= 'Z'):
        maisculos.append(frase[i])
    elif (frase[i] >= 'a') and (frase[i] <= 'z'):
        minusculos.append(frase[i])
    else:
        especiais.append(frase[i])

print('Números:', len(numeros))
print('Maiúsculos:', len(maisculos))
print('Minúsculos:', len(minusculos))
print('Especiais:', len(especiais))

print(numeros)
print(maisculos)
print(minusculos)
print(especiais)
