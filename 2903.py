N = int(input())

k = 2
for i in range(N):
    k += k-1
print(k**2)