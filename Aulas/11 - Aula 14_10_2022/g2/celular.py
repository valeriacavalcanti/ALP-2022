import random

# declarar a tela
tela = []
for i in range(11):
    tela.append([0]*6)

# gerar os toques na tela
for i in range(400):
    linha = random.randint(0,10)
    coluna = random.randint(0,5)
    tela[linha][coluna] += 1

# exibir o status da tela
for i in range(11):
    print(tela[i])

# exibir a quantidade de toques por linha
for i in range(11):
    soma = 0
    for j in range(6):
        soma += tela[i][j]
    print('Linha:', i, '- soma =', soma, '- media =',soma//6)

# exibir a quantidade de toques por coluna
for i in range(6):
    soma = 0
    for j in range(11):
        soma += tela[j][i]
    print('Coluna:', i, '- soma =', soma,'- media =',soma//11)

# maior quantidade de toques registrados em um setor
maior = 0
for i in range(11):
    for j in range(6):
        if (tela[i][j] > maior):
            maior = tela[i][j]
print('Maior quantidade no setor:', maior)

# setor(es) apresentam maior qt de toques na tela
for i in range(11):
    for j in range(6):
        if (tela[i][j] == maior):
            print(i, j)