N,M = map(int,input().split())
a = 0
N_list = []
for q in range(N):
    N_list.append(q+1)


for k in range(M):
    i,j = map(int,input().split())
    a = N_list[i-1]
    N_list[i-1]=N_list[j-1]
    N_list[j-1] = a

for y in range(N):
    print(N_list[y], end=' ')
