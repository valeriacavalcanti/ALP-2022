a,l,p = input().split()
a,l,p = int(a), int(l), int(p)

n = int(input())

if (n <= a) and (n <= l) and (n <= p):
    print("S")
else:
    print("N")