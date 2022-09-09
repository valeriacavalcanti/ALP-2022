# lista de tamanho 8
lista = [0] * 8

# ler os 8 números e armazenar na lista
for i in range(8):
    lista[i] = int(input("Número: "))

# exibir os números, um por linha
for i in range(len(lista)):
    print('indice', i, '-', lista[i])

# exibir os números na ordem inversa
for i in range(len(lista)-1, -1, -1):
    print('indice', i, '-', lista[i])