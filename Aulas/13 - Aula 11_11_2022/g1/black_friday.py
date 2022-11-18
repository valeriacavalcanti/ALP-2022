q_desonesta = 0
q_honesta = 0

for i in range(10):
    antes, durante = input().split()
    antes, durante = float(antes), float(durante)

    if (durante < antes):
        q_honesta += 1
    else:
        q_desonesta += 1

print("honestos: {} ({:.1f}%)".format(q_honesta, q_honesta*10))
print("desonestos: {} ({:.1f}%)".format(q_desonesta, q_desonesta*10))