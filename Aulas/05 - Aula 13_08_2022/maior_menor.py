numero = int(input("Número: "))
maior = numero
menor = numero

for i in range(5):
  numero = int(input("Número: "))
  if (numero > maior):
    maior = numero
  elif (numero < menor):
    menor = numero

print(maior)
print(menor)
