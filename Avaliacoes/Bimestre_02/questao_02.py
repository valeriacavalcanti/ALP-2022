n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

if (n1 > n2) and (n1 > n3):
    print(n1)
else:
    if (n2 > n3):
        print(n2)
    else:
        print(n3)
