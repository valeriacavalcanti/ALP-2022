nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

ma = (nota1 + nota2 + nota3) / 3
mp = (nota1 * 4 + nota2 * 6 + nota3 * 8) / 18

if (ma > mp):
    print('MA')
elif (ma < mp):
    print("MP")
else:
    print("TANTO FAZ")