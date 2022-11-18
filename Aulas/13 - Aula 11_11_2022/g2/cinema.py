lugares = []
qtde = 0

for i in range(10):
    lugares.append([False] * 20)

for i in range(100):
    linha, coluna = input().split()
    linha, coluna = int(linha), int(coluna)

    if (lugares[linha][coluna] == False):
        lugares[linha][coluna] = True
        qtde += 1

print(qtde)