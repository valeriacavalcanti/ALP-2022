'''
Escreva um programa para ler uma frase. Remova todos os excessos de espaços em branco,
deixando apenas um espaço em branco entre as palavras.

Lembre que uma frase não pode começar com espaço em branco, nem terminar.

'''

frase = input("Frase: ")

while ('  ' in frase):
  frase = frase.replace('  ', ' ')

if (frase[0] == ' '):
  frase = frase[1:]

if (frase[len(frase) - 1] == ' '):
  frase = frase[:len(frase)-1]

print(frase, '|', sep='')
