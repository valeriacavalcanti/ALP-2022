aprovados = []
notas = []
soma = 0
qtde = 0

for i in range(40):
    nome = input('Nome: ')
    nota = int(input('Nota: '))
    notas.append(nota)
    if (nota >= 70):
        aprovados.append(nome)

media = sum(notas)/40

for i in range(40):
    if (notas[i] > media):
        qtde += 1

print(aprovados)
print(qtde)
