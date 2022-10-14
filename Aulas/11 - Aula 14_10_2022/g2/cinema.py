# declarar a matriz
cinema = []
for i in range(6):
    cinema.append([False] * 8)

# vender os ingressos
for i in range(8):
    while (True):
        print("Pessoa:", i + 1)
        l, c = input("Linha e coluna: ").split()
        l, c = int(l), int(c)
        if (cinema[l][c] == False):
            cinema[l][c] = True
            print("Lugar vendido com sucesso!")
            break
        else:
            print("Lugar ocupado!")

# exibir o status do cinema
for i in range(6):
    print(cinema[i])