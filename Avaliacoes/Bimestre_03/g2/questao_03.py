notas = []
soma = aprovados = reprovados = 0

for i in range(10):
    notas[i] = int(input("Informe sua nota: "))
    soma = soma + notas[i]
    if (notas[i] >= 70):
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
print(soma, aprovados, reprovados)
