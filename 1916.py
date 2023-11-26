#최소비용 구하기
#다익스트라 알고리즘

import heapq
import sys


input = sys.stdin.readline

N = int(input())
M = int(input())


graph = [[] for i in range(N+1)]
visted = [100000000] * (N+1)

for m in range(M):
    s,e,v = map(int,input().split())
    graph[s].append((e,v))
    
start, end = map(int,input().split())

def djikstra(node):
    heap = []
    heapq.heappush(heap,(0,node))
    visted[node] = 0
    
    while heap:
        value, node = heapq.heappop(heap)
        
        if visted[node] < value:
            continue
        
        for n_node, n_value in graph[node]:
            sum_value = value + n_value

            if visted[n_node] > sum_value:
                heapq.heappush(heap,(sum_value,n_node))
                visted[n_node] = sum_value

djikstra(start)
print(visted[end])