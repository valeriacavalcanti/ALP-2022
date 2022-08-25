import random

secreto = random.randint(1,100)
tentativas = 5

while (True):
    numero = int(input("Chute: "))
    tentativas = tentativas - 1
    if (numero == secreto) or (tentativas == 0):
        break
    if (numero < secreto):
        print("Seu número é menor")
    else:
        print("Seu número é maior")
    print("Você tem {} tentativas".format(tentativas))

print(numero, secreto, tentativas)