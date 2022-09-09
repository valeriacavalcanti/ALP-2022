lista = [0] * int(input("Quantidade: "))

# ler os 6 número e armazenar na lista
for i in range(len(lista)):
    lista[i] = int(input("Número: "))

# exibir os números armazenados na lista
print(lista)

# exibir os números armazenados na lista
# um número por linha
for i in range(len(lista)):
    print(lista[i])

# exibir os números armazenados na lista
# na ordem inversa, um número por linha
print("elementos na ordem inversa")
for i in range(len(lista) - 1, -1, -1):
    print(lista[i])