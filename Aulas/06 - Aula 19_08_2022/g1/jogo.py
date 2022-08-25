import random
secreto = random.randint(0,100)
tentativas = 0
numero = int(input("Chute: "))
while (numero != secreto) and (tentativas<10):
    tentativas = tentativas + 1
    if (numero > secreto):
        print("Seu número é maior")
    else:
        print("Seu número é menor")
    numero = int(input("Chute: "))

if (numero == secreto):
    print("Acertou!")
else:
    print("Perdeu!")
print(numero, secreto)
print("Você tentou {} vezes".format(tentativas))