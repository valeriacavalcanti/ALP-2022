qt_clientes= 0
qt_cupons = 0
maior = -1

while (True):
    valor = float(input())
    if (valor <= 0):
        break
    qt_clientes += 1
    qt_cupons += int(valor // 40)
    if (valor > maior):
        maior = valor

print(qt_clientes)
print(qt_cupons)
print("{:.1f}".format(maior))