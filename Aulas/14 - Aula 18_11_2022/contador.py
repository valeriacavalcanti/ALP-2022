frase = input('Frase: ')
vogais = 'aeiouAEIOU'
qtde = 0

for i in range(len(frase)):
  if (frase[i] in vogais):
    qtde += 1

print(qtde)
