'''
Escreva um programa para ler várias frases. Exiba as letras presentes nas
frases e suas respectivas quantidades.

'''

frase = input("Frase: ")
nova = ''
palavras = frase.split()

for i in range(len(palavras) - 1):
  nova += palavras[i] + ' '

nova += palavras[len(palavras) - 1]

print(frase)
print(nova)
