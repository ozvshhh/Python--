T = int(input())
yy = 0
kk = 0

for i in range(T):
    for i in range(9):
        y , k = map(int,input().split())
        yy += y
        kk += k
    if yy > kk:
        print('Yonsei')
    elif yy < kk:
        print('Korea')
    else:
        print('Draw')