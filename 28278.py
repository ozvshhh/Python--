import sys
from collections import deque
input = sys.stdin.readline
queue = deque([])

n = int(input())

for i in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        queue.append(int(cmd[1]))
    if cmd[0] == 2:
        if queue:
            print(queue.pop())
        else:
            print(-1)
    if cmd[0] == 3:
        print(len(queue))
    if cmd[0] == 4:
        if queue:
            print(0)
        else:
            print(1)
    if cmd[0] == 5:
        if queue:
            print(queue[-1])
        else:
            print(-1)    