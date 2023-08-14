a = list(map(int,input().split()))
p = 0
for i in range(5):
    p += a[i]**2
print(p%10)