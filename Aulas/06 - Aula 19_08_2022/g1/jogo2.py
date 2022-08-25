import random
import time

secreto = random.randint(0,100)
tentativas = 0

while (True):
    numero = int(input("Chute: "))
    time.sleep(2)
    if (numero == secreto) or (tentativas == 10):
        break
    tentativas = tentativas + 1
    if (numero > secreto):
        print("Seu número é maior")
    else:
        print("Seu número é menor")

if (numero == secreto):
    print("acertou")
else:
    print("tente novamente ;-)")

print(numero, secreto)
print("Você tentou {} vezes".format(tentativas))