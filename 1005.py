import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N,K = map(int,input().split())
    times = list(map(int,input().split()))
    rule = [[] for i in range(N+1)]
    for k in range(K):
        x,y = map(int,input().split())
        rule[x].append(y)
    print(rule)