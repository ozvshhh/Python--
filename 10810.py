'''

N - 바구니 갯수
M - 공을 넣을 횟수
i~j - 공을 넣을 바구니의 범위
a - 넣을 공의 번호(1<100)
0은 공이 없는 것
'''

N,M = map(int,input().split())
N_list = []
a_list = []
for i in range(N):
    N_list.append(0)

for k in range(M):
    i,j,a = map(int,input().split())
    for q in range(j-i+1):
        a_list.append(a)
    N_list[i-1:j] = a_list.copy()
    a_list = []
for o in range(N):
    print(N_list[o])
