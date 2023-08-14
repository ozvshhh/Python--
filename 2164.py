import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

num = deque(range(1,n+1,1))

while num:
    if len(num) == 1:
        print(num[0])
        break
    else:
        num.popleft()
        num.append(num.popleft())