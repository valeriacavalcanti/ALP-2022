import random
tela = []
for i in range(10):
    tela.append([0]*6)

for i in range(200):
    linha = random.randint(0,9)
    coluna = random.randint(0,5)
    tela[linha][coluna] += 1

# exibir o status da tela
for i in range(10):
    print(tela[i])

# somar os toques por linha
for i in range(10):
    soma = 0
    for j in range(6):
        soma += tela[i][j]
    media = soma//6
    print('linha',i,'- soma =', soma, '- media =', media)

# somar os toques por coluna
for i in range(6):
    soma = 0
    for j in range(10):
        soma += tela[j][i]
    media = soma//10
    print('coluna',i,' - soma =', soma, '- media =', media)

# descobrir a maior qtde de toques registrados em uma
# célula
maior = 0
for i in range(10):
    for j in range(6):
        if (tela[i][j] > maior):
            maior = tela[i][j]

print('Maior quantidade:', maior)

# células com maior quantidade de toques
for i in range(10):
    for j in range(6):
        if (tela[i][j] == maior):
            print(i, j)