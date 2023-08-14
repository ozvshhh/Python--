'''
정렬 n*logn

6
list = [1,1,1,1]

'''
import sys
input = sys.stdin.readline

N=int(input())

L= list(map(int,input().split()))

dp=[0]*N
check = L[0]

for i in range(1,N):
    if check>L[i]:
        dp[i] = dp[i-1]+1
    else:
        check = L[i]
        dp[i] = 0
 
print(max(dp))
       
"""
0 0 0 0 0 0 0

0 1 0 1 2 3 0


"""
    