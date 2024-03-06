#케빈베이컨
#사람들의 관계를 그래프로 만든다.
#그래프의 최단거리를 구한다.
#최단거리는 그냥 bfs 사용하면 될듯?
#이 문제가 어려운 이유, 인덱스랑 밸류의 사용이 혼재되어 머리가 아픔
#이 문제의 핵심 : 어찌되었건 관계는 연결됨. -> 무조건 거리가 나옴

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

relation = [[] for n in range(N+1)] #1번 유저가 0번 인덱스 쓰는게 꼴받아서;; +1 했음

#한 사람의 케빈베이컨의 수를 구하는 함수
def getKevinNum(user):
  queue = deque() #b3333fs 탐색을 위한 queue
  queue.append(user)
  KevinNums = [0 for n in range(N+1)] #0은 기본값, 0인 값만 queue에 포함될 수 있음.
  KevinNums[user] = -1 # 사용하지 않는 값은 -1로 취급
  KevinNums[0] = -1 # 사용하지 않는 값은 -1로 취급
  while queue:
    main = queue.popleft()
    for obj in relation[main]:
      if KevinNums[obj] == 0:
        queue.append(obj)
        KevinNums[obj] =  1 if KevinNums[main]==-1 else KevinNums[main]+1 #lenth 처리를 어떻게 할 것인가? main 값 +1로 처리해야지
        # print("KevinNums:",KevinNums)
      else:
        continue  
  return sum(KevinNums)+2 #사용하지 않는 -1 값이 2개라 그거 제외하려고 넣음

for m in range(M):
  A,B = map(int,input().split())
  relation[A].append(B)
  relation[B].append(A)

min = 5000
minUser = 0
for n in range(1,N+1):
  num = getKevinNum(n)
  if min > num:
    min = num
    minUser = n

print(minUser)

  

# print(relation)

