numero = int(input("Número: "))
soma = 0
quantidade = 0
for i in range(numero):
    soma = soma + i
    if (i % 4 == 0):
        quantidade = quantidade + 1

print(soma)
print(quantidade)
