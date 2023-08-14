a = input()
h = 10

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        h += 5
    else:
        h += 10
print(h)
