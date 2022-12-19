import funcoes
import matematica

# PROGRAMA PRINCIPAL
letra = 'a'
if (funcoes.e_vogal(letra) == True):
  print("É uma vogal")
else:
  print("Não é uma vogal")

frase = "eu adoro estudar python"
vogais = funcoes.contar_vogais(frase)
print("Quantidade:", vogais)

numeros = [10,20,30,40,50,60]
print(numeros)
print(matematica.somar(numeros))
print(matematica.media(numeros))
