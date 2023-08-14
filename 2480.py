a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a==b==c:
    print(10000+a*1000)
else:
    if (a==b) or (a==c) or (b==c):
        same = a if a==b else (a if a==c else c)
        print(1000+same*100)
    else: #3개 다 다르다.
        max = a if a>b else b
        max = max if max>c else c
        print(max*100)