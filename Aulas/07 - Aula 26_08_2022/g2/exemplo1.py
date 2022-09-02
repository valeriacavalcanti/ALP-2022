soma = 0
qtde = int(input("Quantidade: "))
numeros = [0] * qtde

for i in range(qtde):
    numeros[i] = int(input("Número: "))
    soma = soma + numeros[i]

print("Números:", numeros)
print("Soma:", soma)
media = soma / qtde
print("Média:", media)

# Exibir TODOS os números da lista
print("Todos os números")
for i in range(qtde):
    print(i, numeros[i])

# Exibir os números com valor acima da média da lista
print("Todos os números acima da média da lista")
for i in range(qtde):
    if (numeros[i] > media):
        print(i, numeros[i])