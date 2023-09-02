#2xn 타일링 2

import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+3)

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(3,n+1):
    dp[i] = (dp[i-1] + (dp[i-2] * 2))%10007

print(dp[n])
'''
1. dp 테이블 설정
dp[i] = 가로 길이가 i 일때 직사각형을 채우는 방법의 수

dp[1] = 1
dp[2] = 3
dp[3] = 5

dp[i] = dp[i-1] + (d[i-2]+3)
'''