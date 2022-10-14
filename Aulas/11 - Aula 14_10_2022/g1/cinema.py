# alocar a matriz
lugares = []
for i in range(6):
    lugares.append([False]*6)

# vender ingressos
for i in range(13):
    while (True):
        print("Ingresso:",i)
        l, c = input("Linha e coluna: ").split()
        l, c = int(l), int(c)

        if (lugares[l][c] == False):
            lugares[l][c] = True
            print("Lugar vendido com sucesso!")
            break
        else:
            print("Lugar ocupado!")

print(lugares)