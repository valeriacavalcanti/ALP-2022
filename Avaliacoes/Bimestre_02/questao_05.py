quantidade = 0

for i in range(40):
    nota = int(input("Nota: "))
    if ((nota >= 0) and (nota <= 100)):
        quantidade = quantidade + 1

print(quantidade)
