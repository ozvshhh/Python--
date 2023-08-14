cc = 100
ss = 100

T = int(input())

for i in range(T):
    c,s = map(int,input().split())
    
    if c>s:
        ss -= c
    elif c<s:
        cc -= s
    else:
        pass 
print(cc)
print(ss)
        