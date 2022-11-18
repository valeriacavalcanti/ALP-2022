l,p,a = input().split()
l,p,a = int(l),int(p),int(a)
n = int(input())

if (n > l) or (n > p) or (n > a):
    print("N")
else:
    print("S")