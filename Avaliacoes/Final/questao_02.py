qt = 0
lista = []

email = input('e-mail: ')
while (email.upper() != 'FIM'):
    qt += 1
    parte1, parte2 = email.split('@')
    empresa, filial, br = parte2.split('.')
    if (filial not in lista):
        lista.append(filial)
    email = input('e-mail: ')

print(qt)
print(lista)
