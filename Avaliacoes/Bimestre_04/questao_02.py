votados = []

for i in range(120):
    voto = input('Voto: ').upper()
    if (voto not in votados):
        votados.append(voto)

print(votados)
