qnum = qmai = qmin = qesp = 0

frase = input('Frase: ')

for i in range(len(frase)):
    if (frase[i] >= '0') and (frase[i] <= '9'):
        qnum += 1
    elif (frase[i] >= 'A') and (frase[i] <= 'Z'):
        qmai += 1
    elif (frase[i] >= 'a') and (frase[i] <= 'z'):
        qmin += 1
    else:
        qesp += 1

print('Números:', qnum)
print('Maiúsculos:', qmai)
print('Minúsculos:', qmin)
print('Especiais:', qesp)
