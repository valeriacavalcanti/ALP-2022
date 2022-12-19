# somar os elementos da lista.
# Parâmetros: lista
# Retorno: int ou float
def somar(lista):
  soma = 0
  for i in range(len(lista)):
    soma += lista[i]
  return soma


# Calcular a média dos números da lista.
# Parâmetros: lista
# Retorno: float
def media(lista):
  return somar(lista)/len(lista)


# Encontrar o maior valor da lista.
# Parâmetros: lista
# Retorno: int ou float
def maior(lista):
  m = lista[0]
  for i in range(1, len(lista)):
    if (lista[i] > m):
      m = lista[i]
  return m


# Encontrar o menor valor da lista.
# Parâmetros: lista
# Retorno: int ou float
def menor(lista):
  m = lista[0]
  for i in range(1, len(lista)):
    if (lista[i] < m):
      m = lista[i]
  return m


# Retornar o índice onde está o menor valor.
# Parâmetros: lista
# Retorno: int
def indice_menor_valor(lista):
  m = menor(lista)
  for i in range(len(lista)):
    if (lista[i] == m):
      return i
