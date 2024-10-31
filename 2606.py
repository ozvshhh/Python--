#2606 바이러스

from collections import deque

COM=int(input())
N=int(input())
network = [[] for __ in range(COM+1)]

def bfs():
    count = [True for __ in range(COM+1)]
    queue = deque([])
    queue.append(1)
    rtn = 0

    count[1]=False
    while queue:
        target = queue.popleft()
        for num in network[target]:
            if count[num]:
                #print("num:",num)
                queue.append(num)
                count[num] = False
                rtn += 1 
            else:
                continue
    return rtn

for __ in range(N):
    a,b=map(int,input().split())
    network[a].append(b)
    network[b].append(a)

print(bfs())