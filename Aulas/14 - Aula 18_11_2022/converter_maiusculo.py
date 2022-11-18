nova = ''
frase = input("Frase: ")

for i in range(len(frase)):
  if (frase[i] >= 'a') and (frase[i] <= 'z'):
    nova += chr(ord(frase[i]) - 32)
  else:
    nova += frase[i]

print(frase)
print(nova)
