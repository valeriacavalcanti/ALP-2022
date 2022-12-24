erro = 0
frase = input("Frase: ")
while (len(frase) < 20):
    erro += 1
    frase = input("Frase: ")

print(erro)
print(len(frase))
