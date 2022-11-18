qt_num = qt_min = qt_mai = qt_esp = 0

frase = input("Frase: ")

for i in range(len(frase)):
  if (frase[i] >= '0') and (frase[i] <= '9'):
    qt_num += 1
  elif (frase[i] >= 'A') and (frase[i] <= 'Z'):
    qt_mai += 1
  elif (frase[i] >= 'a') and (frase[i] <= 'z'):
    qt_min += 1
  else:
    qt_esp += 1

print('Tamanho:', len(frase))
print('Maiúsculo:', qt_mai)
print('Minúsculo:', qt_min)
print('Números:', qt_num)
print('Especiais:', qt_esp)
