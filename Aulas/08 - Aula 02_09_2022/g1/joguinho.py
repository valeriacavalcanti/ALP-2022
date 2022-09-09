import random
menor = 0
maior = 100
sorteado = random.randint(menor, maior)
chutes = []
print(sorteado)

chute = int(input("Chute: "))
while (chute != sorteado) and (chute >= menor) and (chute <= maior):
    chutes.append(chute)
    if (chute < sorteado):
        print('seu chute é menor')
        menor = chute
    else:
        print('seu chute é maior')
        maior = chute
    # perguntar o próximo
    chute = int(input("Chute: "))

# jogo encerrou, vamos ver o resultado

if (sorteado == chute):
    print("Ganhou!")
else:
    print("Perdeu!")

# auditoria
print("Sorteado:", sorteado)
print("Chute:", chute)
print("Chutes:", chutes)
print("Intervalo:", menor, maior)