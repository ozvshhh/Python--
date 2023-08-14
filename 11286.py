import sys
import heapq
input = sys.stdin.readline
 
heap = []

T=int(input())
for number in range(T):
    n = int(input())
    if n > 0:
        n = float(n)+0.5
    else:
        n = float(-n)
    #print(heap)
    if n == 0:
        if len(heap) == 0:
            print(0)
        else:
            a = heapq.heappop(heap)
            if a%1 == 0.5:
                print(int(a-0.5))
            else: 
                print(-int(a))
    else:
        heapq.heappush(heap,n)