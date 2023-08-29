#가장 긴 증가하는 부분수열
import sys
input = sys.stdin.readline

A = int(input())
A_list = list(map,int,input().split())

dp = [0]*1001

for a in range(1,len(A_list)):
    for i in range(i,len(A_list)):
        

'''
어떻게 이게 dp로 풀리는거지?

중요한것? 증가했는가
숫자가 증가했으면 가능성이 있겠지?

10 20 10 30 20 50

10 20 30 50 가능
10 20 가능
10 30 50
커지면 길이 증가
줄어들면


'''