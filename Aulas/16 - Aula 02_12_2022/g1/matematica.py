# Somar os elementos da lista.
# parâmetros: lista
# retorno: int ou float
def somar(lista):
  soma = 0
  for i in range(len(lista)):
    soma += lista[i]
  return soma


# Calcular a média dos elementos da lista.
# parâmetros: lista
# retorno: float
def media(lista):
  return somar(lista) / len(lista)
