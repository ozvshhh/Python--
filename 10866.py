import sys
from collections import deque
input = sys.stdin.readline
queue = deque([])

n = int(input())

for i in range(n):
    cmd = list(input().split())
    if cmd[0] == "push_front":
        queue.appendleft(int(cmd[1]))
    if cmd[0] == "push_back":
        queue.append(int(cmd[1]))
    if cmd[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    if cmd[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    
    if cmd[0] == "size":
        print(len(queue))
    if cmd[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    if cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    if cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)    