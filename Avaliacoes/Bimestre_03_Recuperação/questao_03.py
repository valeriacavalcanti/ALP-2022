# maior = menor = 0
maior = menor = int(input('Número: '))

# for i in range(6):
for i in range(5):
  numero = int(input("Número: "))
  # if (numero < maior):
  if (numero > maior):
    maior = numero
  # elif (numero > menor):
  elif (numero < menor):
    menor = numero

print(maior)
print(menor)
