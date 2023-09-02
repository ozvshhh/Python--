#가장 긴 증가하는 부분수열
import sys
input = sys.stdin.readline

A = int(input())
A_list = [0] + list(map(int,input().split()))

dp = [0]*(A+1)

for i in range(1,A+1):
    for j in range(i):
        if A_list[i] > A_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

'''
시간복잡도로 접근
1000 * 1000 -> 1000000 백만(N**2 가능 )
어떻게 이게 dp로 풀리는거지?
-> 김현준님의 강의:
10 20 10 30 20 50 10 10 10 10 40
 1  2  1  3  2  4  1  1  1  1  4
dp[i] = i 번쨰 숫자를 마지막으로 갖는 부분수열의 최대길이
dp[i]를 구할 때에 완전탐색을 해야하는가?
증가했다면 탐색을진행하자


중요한것? 증가했는가
숫자가 증가했으면 가능성이 있겠지?

10 20 10 30 20 50

10 20 30 50 가능
10 20 가능
10 30 50
커지면 길이 증가
줄어들면


'''