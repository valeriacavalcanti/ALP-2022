qt = 0
erradas = []

while (True):
    nota = int(input("Nota: "))
    if (nota >= 0) and (nota <= 100):
        break
    erradas.append(nota)

for i in range(len(erradas)):
    if (nota % erradas[i] == 0):
        qt += 1

print(erradas)
print(qt)