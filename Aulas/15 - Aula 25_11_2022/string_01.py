'''
Escreva um programa para ler 10 frases. Calcular e exibir:
Quantidade de letras
Quantidade de dígitos numéricos
Quantidade de palavras
Quantidade de vogais

'''


qt_letras = qt_vogais = qt_numeros = qt_palavras = 0

for i in range(2):
  frase = input("Frase: ")
  for j in range(len(frase)):
    if (frase[j].isalpha()):
      qt_letras += 1
      if (frase[j] in 'aeiouAEIOU'):
        qt_vogais += 1
    elif (frase[j].isdigit()):
      qt_numeros += 1
  qt_palavras += len(frase.split())

print(qt_letras, qt_vogais, qt_numeros, qt_palavras)
