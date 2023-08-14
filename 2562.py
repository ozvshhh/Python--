a = []
b = []
for i in range(9):
    a.append(int(input()))
b = a.copy()
b.sort()
print(b[8])
print(a.index(b[8]+1))
