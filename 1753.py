#최단경로
import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

graph = [[]for i in range(V+1)]
for e in range(E):
    u,v,w = tuple(map(int,input().split()))
    graph[u].append((w,v))
#print(graph)

visited = [6000000001]*(V+1)
#print(visted)
#print(distance)

#print(graph)
def djikstra(node):
    heap = []
    #(가중치,노드)
    heapq.heappush(heap,(0,node))
    visited[node] = 0
    
    while heap:
        weight,node = heapq.heappop(heap)
        
        for w,n in graph[node]:
            n_weight = weight + w
            if n_weight < visited[n]:
                heapq.heappush(heap,(n_weight,n))
                visited[n] = n_weight
                
djikstra(start)
for i in range(1,V+1):
    if visited[i] == 6000000001:
        print("INF")
    else:
        print(visited[i])