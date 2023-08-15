#11497 통나무 건너뛰기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N = int(input())
    logs = sorted(map(int,input().split()))
    
    
    output = 0
    
    for i in range(2,N):
        diff = logs[i] - logs[i-2]
        if diff > output:
            output = diff
    print(output)

'''

진행방향이 2개이다.



2 4 5 7 9 이거면
2
4 2 5
7 4 2 5 9 이렇게 배치하면 됨

'''