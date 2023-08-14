#11000 강의실 배정

import sys
input = sys.stdin.readline

import heapq

II=lambda:int(input())
LI=lambda:list(map(int,input().split()))


a = []
heap = []
heapq.heappush(heap,0)

T=II()
for i in range(T):
    start,end = LI()
    a.append((start,end))
a.sort(key=lambda x:x[1])
a.sort(key=lambda x:x[0])

#print(a)

for i in range(T):
    if a[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,a[i][1])
    else:
        heapq.heappush(heap,a[i][1])
print(len(heap))

'''
1초안에 문제를 풀어야하고
메모리가 굉장히 작다.
주어진 자원이 굉장히 적음으로
이 문제는 heap을 이용해서 풀어야한다
와 안되노;;
정렬은 안해서 안됬다.
end 값을 먼저 정렬하고
start 값을 나중에 정렬해야 문제가 풀리더라

왜?? - start 값이 우선순위를 가지지?
강의실을 빠르게 매칭하려면
end 값이랑 start 값이랑 딱 맞아 떨어지는
끝나자마자 시작하는 데이터를 연결해줘야한다.
start 값이 낮은 것 부터 탐색을 하면 건너뛰는 것 없이
직전 end값에 가장 근접한 start 값을 탐색할 수 있다
'''