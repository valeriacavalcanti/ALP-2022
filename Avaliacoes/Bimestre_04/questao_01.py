argentina = franca = erro = 0

for i in range(40):
    voto = input('Informe seu voto: ')
    if (voto == 'ARGENTINA'):
        argentina += 1
    elif (voto == 'FRANÇA'):
        franca += 1
    else:
        erro += 1

if (argentina > franca):
    print('Argentina é favorita')
elif (franca > argentina):
    print('França é favorita')
else:
    print('Não existe favorita')

print('Votos errados:', erro)
