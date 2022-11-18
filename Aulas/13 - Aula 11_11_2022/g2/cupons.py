qt_cupons = 0
qt_clientes = 0
maior = -1

valor = float(input())
while (valor > 0):
    qt_clientes += 1
    qt_cupons += int(valor // 40)
    if (valor > maior):
        maior = valor

    valor = float(input())

print(qt_clientes)
print(qt_cupons)
print("{:.1f}".format(maior))