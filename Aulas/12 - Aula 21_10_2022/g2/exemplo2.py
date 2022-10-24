'''
    ESCREVA UM PROGRAMA PARA LER 01(UM) SÍMBOLO, VERIFICAR E EXIBIR SE É:
    - SÍMBOLO NUMÉRICO
    - LETRA MAIÚSCULA
    - LETRA MINÚSCULA
    - CARACTERE ESPECIAL
'''

s = input('Símbolo: ')
if (s >= '0') and (s <= '9'):
    print('Símbolo numérico')
elif (s >= 'A') and (s <= 'Z'):
    print('Letra maiúscula')
elif (s >= 'a') and (s <= 'z'):
    print('Letra minúscula')
else:
    print('Caractere especial')