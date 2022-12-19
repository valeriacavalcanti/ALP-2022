# Verificar se um símbolo é vogal.
# Parâmetros: simbolo(str)
# Retorno: bool
def e_vogal(simbolo):
  if (simbolo in 'AEIOUaeiou'):
    return True
  else:
    return False


# Calcular a quantidade de vogais.
# Parâmetros: string
# Retorno: int
def contar_vogais(st):
  qtde = 0
  for i in range(len(st)):
    if (e_vogal(st[i]) == True):
      qtde += 1
  return qtde
