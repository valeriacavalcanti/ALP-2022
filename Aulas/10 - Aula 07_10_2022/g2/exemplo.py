#matriz = []
#for i in range(5):
#    matriz.append([0] * 4)

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]

print(matriz)
print('---------')
for i in range(len(matriz)):
    print(matriz[i])
print('----------')
for linha in matriz:
    print(linha)
print('----------')
for i in range(5):
    for j in range(4):
        #print(i, j, matriz[i][j])
        print(matriz[i][j], end=' ')
    print()