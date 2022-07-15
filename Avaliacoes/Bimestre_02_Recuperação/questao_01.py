quantidade = 0
soma = 0

for i in range(20):
    numero = int(input("Informe um número: "))
    if (numero > 0) and (numero < 100):
        quantidade = quantidade + 1
    soma = soma + numero

# quantidade de números entre (0,100)
print(quantidade)
# média dos números lidos
print(soma/20)
