a, b, C = map(int,input().split())

for c in range(C):
    if a == b:
        break
    a = a ^ b
print(a)