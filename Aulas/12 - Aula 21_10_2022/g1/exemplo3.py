simbolo = input('Símbolo: ')

if (simbolo >= '0') and (simbolo <= '9'):
    print('Símbolo numérico')
elif (simbolo >= 'A') and (simbolo <= 'Z'):
    print('Letra maiúscula')
elif (simbolo >= 'a') and (simbolo <= 'z'):
    print('Letra minúscula')
else:
    print('Caractere especial')