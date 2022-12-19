'''
Escreva um programa para ler uma frase e substituir todas as ocorrências de vogais por “*” (asterisco).
Ao final exiba:
Quantidade de vogais encontradas.

'''

frase = input("Frase: ")
nova = ''

for i in range(len(frase)):
  if (frase[i] in 'aeiouAEIOU'):
    nova += '*'
  else:
    nova += frase[i]

print(frase)
print(nova)
