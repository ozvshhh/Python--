#토마토1
#시간초과
#deque 쓰면 시간 단축 됨 !!

import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
box = []
queue = deque()

for i in range(N):
    box.append(list(map(int,input().split())))

def findOne():
    idx_one = []
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                idx_one.append((i,j))
    return idx_one

queue = findOne()


def bfs(queue):
    queue = deque(queue)
    queue_last = None
    while queue:
        now_idx = queue[0]
        queue.popleft()
        researcher = [(1,0),(0,1),(-1,0),(0,-1)]
        if 0 <= now_idx[0]-1 <N:
            pass
        else:
            researcher.remove((-1,0))
        
        if 0 <= now_idx[0]+1 <N:
            pass
        else:
            researcher.remove((1,0))
        
        if 0 <= now_idx[1]-1 <M:
            pass
        else:
            researcher.remove((0,-1))
        
        if 0 <= now_idx[1]+1 <M:
            pass
        else:
            researcher.remove((0,1))
        
        for i in researcher:
            if box[now_idx[0]+i[0]][now_idx[1]+i[1]] == 0:
                box[now_idx[0]+i[0]][now_idx[1]+i[1]] = box[now_idx[0]][now_idx[1]] + 1
                queue.append((now_idx[0]+i[0],now_idx[1]+i[1]))
                queue_last = (now_idx[0]+i[0],now_idx[1]+i[1])
            else:
                pass
        #print(queue)
        #print(box)
        if len(queue) == 0:
            break
        else:
            continue
    minusOne = False
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                minusOne = True
    if minusOne == True:
        return -1
    if queue_last == None:
        return 0
    else:
        return box[queue_last[0]][queue_last[1]] -1
        
j = bfs(queue)
print(j)