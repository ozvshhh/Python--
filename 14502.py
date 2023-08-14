import sys
from itertools import product,combinations
import copy
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
lab = []
for i in range(N):
    lab.append(list(map(int,input().split())))

#print(lab)

n_list = [i for i in range(N)]
m_list = [i for i in range(M)]


def findTwo():
    idx_virus = []
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                idx_virus.append((i,j))
    return idx_virus
idx_virus = findTwo()

def bfs(queue,lab2):
    queue = deque(idx_virus) 
    while queue:
        #print(queue)
        #print(lab2)
        idx = queue.popleft()
        searcher = [(1,0),(-1,0),(0,1),(0,-1)]
        
        if (0 <= idx[0]+1 <N):
            pass
        else:
            searcher.remove((1,0))
        if (0 <= idx[0]-1 <N):
            pass
        else:
            searcher.remove((-1,0))
        if(0 <= idx[1]+1 <M):
            pass
        else:
            searcher.remove((0,1))
        if (0 <= idx[1]-1 <M):
            pass
        else:
            searcher.remove((0,-1))
        
        for i,j in searcher:
            if lab2[idx[0]+i][idx[1]+j] == 0:
                lab2[idx[0]+i][idx[1]+j] = 2
                queue.append((idx[0]+i,idx[1]+j))
            else:
                continue
    #print(lab2)
               
    #안전영역 세기
    count = 0
    for i in range(N):
        for j in range(M):
            if lab2[i][j] == 0:
                count += 1
    return count

pos_list = [i for i in product(n_list,m_list,repeat=1)]

#바이러스가 있는 곳에 벽 세우는 경우 제거
for v in idx_virus:
    if v in pos_list:
        pos_list.remove(v)
        
#기존에 벽이 있던 곳에 벽 세우는 경우 제거
#벽 위치 확인
lab_wall_pos = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 1:
            lab_wall_pos.append((i,j))
#벽 세우는 경우에서 벽 위치 제거
for wall_pos in lab_wall_pos:
    if wall_pos in pos_list:
        pos_list.remove(wall_pos)



Max = 0
for walls in combinations(pos_list,3):
    lab2 = copy.deepcopy(lab)
    for i_wall,j_wall in walls:
        lab2[i_wall][j_wall] = 1
    safe = bfs(idx_virus,lab2)
    
    if safe > Max:
        #print(walls)
        #print(lab2)
        Max = safe
print(Max)
