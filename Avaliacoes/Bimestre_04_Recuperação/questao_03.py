qt = 0

for i in range(30):
    matricula = input('Matrícula: ')
    if (matricula[5] == '7') and (matricula[6] == '8'):
        qt += 1

print(qt)
