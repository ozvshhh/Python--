#유기농배추
#인접한 블럭의 수 구하기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
  
  M,N,K = map(int,input().split())
  cabbage = [[0 for n in range(N) ] for m in range(M)]
  for k in range(K):
    X,Y = map(int,input().split())
    cabbage[X][Y] = 1
  #선형탐색
  #선형탐색중 1을 발견하면
  #queue에 값을 넣고 bfs 하기
  #bfs가 끝나면 다시 선형탐색
  count = 0
  def countCabbage(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
      posX,posY = queue.popleft()
      for add in [(0,1),(1,0),(-1,0),(0,-1)]:
        findX = posX+add[0]
        findY = posY+add[1]
        if 0 <= findX < M and 0 <= findY < N:
          if cabbage[findX][findY] == 1:
            queue.append((findX,findY))
            cabbage[findX][findY] = 0
  
  for m in range(M):
    for n in range(N):
      if cabbage[m][n] == 1:
        count += 1
        countCabbage(m,n)
  print(count)
        
        
          
    
  # print(cabbage)
  

        
