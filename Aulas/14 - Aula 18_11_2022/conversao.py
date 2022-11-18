frase = list(input('Frase: '))

for i in range(len(frase)):
  if (frase[i] >= 'a') and (frase[i] <= 'z'):
    frase[i] = chr(ord(frase[i]) - 32)

print(frase)
