qt_honesto = qt_desonesto = 0

for i in range(10):
    antes, durante = input().split()
    antes, durante = float(antes), float(durante)

    if (durante < antes):
        qt_honesto += 1
    else:
        qt_desonesto += 1

print("honestos: {} ({:.1f}%)".format(qt_honesto, qt_honesto * 10))
print("desonestos: {} ({:.1f}%)".format(qt_desonesto, qt_desonesto * 10))