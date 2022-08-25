import random

tentativas = 4
secreto = random.randint(1,100)
numero = int(input('Chute: '))
while (numero != secreto) and (tentativas > 0):
    if (numero < secreto):
        print("Seu número é menor")
    else:
        print("Seu número é maior")
    print("Você tem {} tentativas".format(tentativas))
    tentativas = tentativas - 1
    numero = int(input('Chute: '))

print(numero, secreto)
if (numero == secreto):
    print("Acertou!")
else:
    print("Tente novamente!  ;-)")