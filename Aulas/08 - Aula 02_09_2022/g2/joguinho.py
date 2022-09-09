import random

chutes = [] # armazenas os chutes do jogador (tentativas)
menor = 100
maior = 200
sorteado = random.randint(menor, maior)
#print(sorteado)

chute = int(input("Chute: "))
while (chute != sorteado) and (chute >= menor) and (chute <= maior):
    chutes.append(chute)
    if (chute < sorteado):
        print("Seu chute é menor")
        menor = chute
    else:
        print("Seu chute é maior")
        maior = chute
    chute = int(input("Chute: "))

print(chute, sorteado, menor, maior)
print(chutes)