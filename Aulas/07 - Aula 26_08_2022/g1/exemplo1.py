qtde = int(input("Quantidade: "))
lista = [0] * qtde
soma = 0

# LER OS VALORES
for i in range(qtde):
    lista[i] = int(input("Valor: "))
    soma = soma + lista[i]

print("lista:", lista)
print("soma:",soma)
media = soma/qtde
print("media:",media)

# EXIBIR TODOS OS VALORES
print("Valores da lista")
for i in range(qtde):
    print(i, lista[i])

# EXIBIR OS VALORES ACIMA DA MÉDIA
print("Valores acima da média")
for i in range(qtde):
    if (lista[i] > media):
        print(lista[i])