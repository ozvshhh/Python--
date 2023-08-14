import sys
input = sys.stdin.readline

N,M = map(int,input().split())

maze = [[] for i in range(N)]

for i in range(N):
    a = input()[0:M]
    for j in a:
        maze[i].append(int(j))
#print(maze)
mazetype = 0
if maze[N-1][M-2] == 1 and maze[N-2][M-1] == 1:
    mazetype = 1

def bfs():
    queue = [(0,0)]
    stack = 0
    count = 1
    while queue:
        idx = queue.pop(0)
        searcher = [(1,0),(0,1),(-1,0),(0,-1)]
        if 0 <= idx[0] + 1 <N:
            pass
        else:
            searcher.remove((1,0))
        if 0 <= idx[0] - 1 <N:
            pass
        else:
            searcher.remove((-1,0))
        if 0 <= idx[1] + 1 < M:
            pass
        else:
            searcher.remove((0,1))
        if 0<= idx[1] - 1 < M:
            pass
        else:
            searcher.remove((0,-1))
        
        for i in searcher:
                #if (idx[0]+i[0],idx[1]+i[1]) == (N-1,M-1):

                
                    if maze[idx[0]+i[0]][idx[1]+i[1]] == 1:
                        maze[idx[0]+i[0]][idx[1]+i[1]] = maze[idx[0]][idx[1]]+1
                        count = maze[idx[0]+i[0]][idx[1]+i[1]]
                        #print("queue,append",(idx[0]+i[0],idx[1]+i[1]))
                        #print(maze)
                        queue.append((idx[0]+i[0],idx[1]+i[1]))
                        #print(maze)
                    else:
                        continue

    # if mazetype == 1:
    #     #print("type 1")
    #     return count + 1
    # else:
    #     return count
    
    return maze[N-1][M-1]
w = bfs()
print(w)

#pop 위치를 while 밑에 둘 것
#https://www.acmicpc.net/source/share/703d275d005649c09ced332500085ed0
#배열 2개 깔고 방문처리 하는 문제도 있음