codigo_peca1 = input("Código peça 1:")
qtde_peca1 = int(input("Qtde peça 1: "))
valor_peca1 = float(input("Valor peça 1: "))

codigo_peca2 = input("Código peça 2:")
qtde_peca2 = int(input("Qtde peça 2: "))
valor_peca2 = float(input("Valor peça 2: "))

total = qtde_peca1 * valor_peca1 + qtde_peca2 * valor_peca2

print("Valor final =", total)
