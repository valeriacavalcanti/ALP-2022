qt = 0
erradas = []

nota = int(input('Nota: '))
while (nota < 0) or (nota > 100):
    erradas.append(nota)
    nota = int(input('Nota: '))

for i in range(len(erradas)):
    if (nota % erradas[i] == 0):
        qt += 1

print(qt)

# exibir as notas erradas
print(erradas)

for i in range(len(erradas)):
    print(erradas[i])

print("será que funciona?")
for elemento in erradas:
    print(elemento)