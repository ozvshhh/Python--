from collections import deque

N,M = map(int,input().split())

org_graph = []

for i in range(N):
    org_graph.append(input())

graph = [[[]for i in range(N)]for i in range(M)]

for i in range(N):
    for j in range(M):
        if org_graph[i][j] == "#":
            graph[i][j] = -2
        elif org_graph[i][j] == "J":
            graph[i][j] = 1
        elif org_graph[i][j] == "F":
            graph[i][j] = -1
        elif org_graph[i][j] == ".":
            graph[i][j] = 0
print(graph)

def findObject(graph:list,object:int):
    answer = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == object:
               answer.append((i,j))
    return(answer) 
print(findObject(graph,-1))

def bfs():
    queue_jihun = deque()
    queue_fire = deque()
    
    #사람 찾아 큐에 넣기
    queue_jihun.append(findObject(graph,1)[0])
    #불찾아 큐에 넣기
    for fire in findObject(graph,-1):
        queue_fire.append(fire)
    
    searcher = [(-1,0),(1,0),(0,-1),(0)]
    
    #사람이 먼저다
    while queue_jihun:
        jihun = queue_jihun.popleft()
        
        if 0 <= jihun[0] + searcher[0] :
            