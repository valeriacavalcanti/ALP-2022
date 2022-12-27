soma = 0
maior = -1
menor = 11

for i in range(10):
    valor = int(input('Nota: '))
    soma += valor

    if (valor > maior):
        maior = valor
    if (valor < menor):
        menor = valor

nota = (soma - maior - menor) / 8

print(menor, maior)
print(nota)
