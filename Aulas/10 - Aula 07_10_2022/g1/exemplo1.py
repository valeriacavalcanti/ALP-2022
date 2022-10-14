matriz = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

#matriz = []
#for i in range(4):
#    matriz.append([0] * 3)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(i, j, matriz[i][j])

print(matriz)