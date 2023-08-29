#파도반수열

import sys
input = sys.stdin.readline


T = int(input())

for t in range(T):
    n = int(input())

    dp = [0]*(n+6)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    dp[6] = 3

    for i in range(7,n+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[n])