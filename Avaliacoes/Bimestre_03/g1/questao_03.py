soma = 0
aprovados = 0
reprovados = 0
nota = int(input("Informe sua nota: "))
while (nota >= 0) and (nota <= 100):
    soma = soma + nota
    if (nota >= 70):
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
print(soma, aprovados, reprovados)
