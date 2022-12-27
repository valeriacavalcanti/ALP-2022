l1, l2, l3, l4 = input("Lados: ").split()
l1, l2, l3, l4 = int(l1), int(l2), int(l3), int(l4)

if (l1 == l2) and (l1 == l3) and (l1 == l4):
    print('sim')
else:
    print('não')
