frase = input('Frase: ')
minuscula = maiuscula = ''

# letras minúsculas
for i in range(len(frase)):
    if (frase[i] >= 'A') and (frase[i] <= 'Z'):
        minuscula += chr(ord(frase[i]) + 32)
    else:
        minuscula += frase[i]

# letras maiúsculas
for i in range(len(frase)):
    if (frase[i] >= 'a') and (frase[i] <= 'z'):
        maiuscula += chr(ord(frase[i]) - 32)
    else:
        maiuscula += frase[i]

print(minuscula)
print(maiuscula)
print(frase)
