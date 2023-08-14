import sys
import heapq
input = sys.stdin.readline
 
heap = []

T=int(input())
for number in range(T):
    n = int(input)
    if 
    #print(heap)
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,n)