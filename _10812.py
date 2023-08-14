N, M = map(int,input().split())

bag = []
save = []

for p in range(N):
    bag.append(p+1)

for p in range(M):
    b,m,e= map(int,input().split())
    
    for q in range(m-b):
        save.append(bag[q-1])
        
    for q in range(m-b):
        bag.pop(b-1+q)
    
    for q in range(len(save)):
        bag.append(save[q])
    
print(bag)