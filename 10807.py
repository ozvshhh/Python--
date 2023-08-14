
N, X = map(int,input().split())
a = []
a = list(map(int,input().split()))
a.sort()

for i in range(N):
    if a.index(i) > X:
    break
        
