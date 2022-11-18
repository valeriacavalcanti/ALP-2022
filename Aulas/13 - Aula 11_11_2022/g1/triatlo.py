total = 0

for i in range(3):
    h,m,s = input().split(":")
    h,m,s = int(h),int(m),int(s)
    total += (h*3600) + (m*60) + s

h = total // 3600
m = (total % 3600) // 60
s = (total % 3600) % 60

print(h,m,s,sep=':')
#print("{}:{}:{}".format(h,m,s))