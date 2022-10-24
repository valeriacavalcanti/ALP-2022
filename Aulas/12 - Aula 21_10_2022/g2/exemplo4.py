'''
    ESCREVA UM PROGRAMA PARA LER 01(UMA) FRASE, EXIBIR:
    - SÍMBOLOS NUMÉRICOS
    - LETRAS MAIÚSCULAS
    - LETRAS MINÚSCULAS
    - CARACTERES ESPECIAIS
'''
lnum = []
lmai = []
lmin = []
lesp = []

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= '0') and (frase[i] <= '9'):
        lnum.append(frase[i])
    elif (frase[i] >= 'A') and (frase[i] <= 'Z'):
        lmai.append(frase[i])
    elif (frase[i] >= 'a') and (frase[i] <= 'z'):
        lmin.append(frase[i])
    else:
        lesp.append(frase[i])

print('Números:', lnum)
print('Maiúsculos:', lmai)
print('Minúsculos', lmin)
print('Caracteres especiais:', lesp)