#피보나치
#1따로 2따로 2개 돌려볼까?

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    dp0 = [0]*(n+2)
    dp1 = [0]*(n+2)

    dp0[0]=1 
    dp0[1]=0
    for i in range(2,n+1):
        dp0[i] = dp0[i-1] + dp0[i-2]

    dp1[0]=0 
    dp1[1]=1
    for i in range(2,n+1):
        dp1[i] = dp1[i-1] + dp1[i-2]
        

    print(dp0[n],dp1[n])
'''
피보나치수열
0
1
2 (1+0)p
3 (1+0+1)
4 (1+0+1+1+0)
5 (10110101)
'''