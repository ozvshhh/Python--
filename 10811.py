N_list = []
S_list = []

N,M = map(int,input().split())

for q in range(N):
    N_list.append(q+1)

for u in range(M):
    S_list = []
    i,j = map(int,input().split())
    for p  in range(j-i+1):
        S_list.append(N_list[j-1-p])
    del N_list[i- 1:j]
    S_list.reverse()
    for r in range(len(S_list)):
        N_list.insert(i-1,S_list[r])

for w in range(N):
    print(N_list[w], end =' ')
