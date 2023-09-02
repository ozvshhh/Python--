import sys
input = sys.stdin.readline

N,K = map(int,input().split())

dp = [[]for i in range(13)]

dp[1].append("1")
dp[2]=["1+1","2"]
dp[3]=["1+1+1","1+2","2+1","3"]

for i in range(4,N+1):
    count = 4
    for j in range(i-3,i):
        count -= 1
        for k in range(len(dp[j])):
            dp[i].append(str(count)+"+"+dp[j][k])

for u in range(len(dp)):
    dp[u].sort()

if len(dp[N]) >= K:
    print(dp[N][K-1])
else:
    print(-1)
            
'''
1 2 3 더하기
2차원 배열을 써보자

11까지 밖에 없어서 은근 쉬울지도 - > 어렵습니다 어려워요..

dp[i][j] <- i:합, j:몇번째 순서

i = 1.
1
i = 2.
1+1 , 2
i = 3
1+1+1, 1+2, 2+1, 3
i=4
1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1 
i=5
1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+1+3, 1+2+1+1, 1+2+2, 1+3+1, 2+1+1+1, 2+1+2, 2+2+1, 2+3, 3+1+1, 3+2

j번째 숫자를 구하는 방법을 생각해보자..
i=4일때 
1로 시작하는 수: 4개
2로 시작하는 수: 2개
3로 시작하는 수: 1개

i=5
1 : 7
    1 : 4
        1 : 2
            1 : 1
        2 : 1
    2 : 2
        1 : 1
    3 : 1
2: 4
    1: 2
        1: 1
    2: 1
3: 2
    3: 1

dp[i]값에 영향을 받는다.
dp[i]값 거꾸로 수열

dp 이차원배열 i:더하는 경우의 수, j:더하는 경우를 배열로 저장

'''