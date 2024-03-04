from copy import deepcopy
from collections import deque

N,M,V = map(int,input().split())

graph = [[]for _ in range(N+1)]


def fill_graph(start,end):
    graph[start].append(end)


for m in range(M):
    start, end = map(int,input().split())  
    fill_graph(start,end)

#print(graph)

def dfs():
    stack = [V]
    ans = []
    
    while stack:
        target = stack.pop()
        if target not in ans:
            ans.append(target)
        
        for search in sorted(graph[target],reverse=True):
            stack.append(search)
                
    return ans

print(dfs())

