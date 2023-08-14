T = int(input())
for i in range(T):
    H,W,N = map(int,input().split())
    a,b = 0,0

    if N%H == 0:
        a = H
    else:
        a = N%H
    
    if N%H == 0:
        b = N//H
    else:
        b = (N//H)+1
    
    a = str(a)
    b = str(b)
    
    if len(b)==2:
        print(a+b)
    else:
        print(a+'0'+b)
