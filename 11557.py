T = int(input())
for i in range(T):
    t = int(input())
    
    name = []
    soju = []
    for i in range(t):
        a,b = input().split()
        b = int(b)
        name.append(a)
        soju.append(b)
        
    print(name[soju.index(max(soju))])