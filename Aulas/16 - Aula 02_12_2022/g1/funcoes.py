# função para verificar se um determinado símbolo
# é uma vogal
# retorno: bool
def e_vogal(simbolo):
  if (simbolo in 'AEIOUaeiou'):
    return True
  else:
    return False


# Função para calcular a quantidade de
# vogais em uma string
# retorna: int
def contar_vogais(st):
  qtde = 0
  for i in range(len(st)):
    if (e_vogal(st[i]) == True):
      qtde += 1

  return qtde
