import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int,input().split())
box = [[] for i in range(H)]

#입력받기
for h in range(H):
    for n in range(N):
        line = list(map(int,input().split()))
        box[h].append(line)

#print(box)

#토마토 찾기
def findTomato(box):
    idx_one = []
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    box[h][n][m] = 2
                    idx_one.append((h,n,m))
    if idx_one:
        return idx_one
    else:
        return False


queue = findTomato(box)
#print(queue)



def dfs(queue):
    def checkType():
        for h in range(H):
            for n in range(N):
                for m in range(M):
                    if box[h][n][m] == 0:
                        return 1
        return 0
    
    
    boxtype = checkType()       
    queue = deque(queue)
    queue_last = False
    while queue:
        searcher = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
        h,n,m = queue.popleft()
        #건전성 탐색
        if 0<=h+1<H:
            pass
        else:
            searcher.remove((1,0,0))
        if 0<=h-1<H:
            pass
        else:
            searcher.remove((-1,0,0))
        if 0<=n+1<N:
            pass
        else:
            searcher.remove((0,1,0))
        if 0<=n-1<N:
            pass
        else:
            searcher.remove((0,-1,0))
        if 0<=m+1<M:
            pass
        else:
            searcher.remove((0,0,1))
        if 0<=m-1<M:
            pass
        else:
            searcher.remove((0,0,-1))
        
        for i,j,k in searcher:
            if box[h+i][n+j][m+k] == 0:
                box[h+i][n+j][m+k] = box[h][n][m] + 1
                queue.append((h+i,n+j,m+k))
                queue_last = (h+i,n+j,m+k)
            else:
                continue
        
    if boxtype == 0:
        return 0

    
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 0:
                    return -1
    
        
    return box[queue_last[0]][queue_last[1]][queue_last[2]] -2

if queue == False:
    print(-1)
else:
    print(dfs(queue))