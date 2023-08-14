N, X = map(int,input().split())
a =[]
a = list(map(int,input().split()))
for i in range(len(a)):
    if a[i] < X:
        print(a[i],end=' ')
    else:
        continue
