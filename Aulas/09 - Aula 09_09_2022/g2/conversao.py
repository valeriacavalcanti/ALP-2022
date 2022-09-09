lista = []
soma = 0

digito = int(input("Dígito binário: "))
while (digito == 0) or (digito == 1):
    lista.append(digito)
    digito = int(input("Dígito binário: "))

print(lista)

tam = len(lista)
for i in range(tam):
    bit = lista[i]
    soma = soma + (bit * 2 ** (tam - 1 - i))

print(soma)