while (True):
  frase = input("Frase: ")

  # converter para minúsculo
  nova = ''
  for i in range(len(frase)):
    if (frase[i] >= 'A') and (frase[i] <= 'Z'):
      nova += chr(ord(frase[i]) + 32)
    else:
      nova += frase[i]

  if (nova == 'fim'):
    break

print(frase)
print(nova)
