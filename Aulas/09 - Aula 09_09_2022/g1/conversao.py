lista = []
soma = 0

num = int(input("Dígito: "))
while (num == 0) or (num == 1):
    lista.append(num)
    num = int(input("Dígito: "))

print(lista)
q = len(lista)
for i in range(q):
    soma = soma + (lista[i] * (2 ** (q - 1 - i)))

print(soma)