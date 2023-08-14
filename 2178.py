import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
list1 = []
for i in range(N):
    list1.append(input()[0:M])
#print(list1)

maze = [[] for i in range(N)]

for i in range(N):
    for j in range(M):
        maze[i].append(int(list1[i][j]))
#print(maze)

#bfs를 위한 queue 생성
queue = [(0,0)]
log = [(0,0)] # list 쓰지말고 set 쓰기
#길이 판단을 위한 lenth 생성
lenth = 1   

#하단,우측 값의 정당성 판단
#상단,우측 값의 정당성 판단

while True:
    for k in queue: #길이가 0이 아닐 때 까지로 바꾸기 for문 안쓰고
        for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
            if 0 <= queue[0][0] + i < N:
                if 0 <= queue[0][1] + j < M :
                    
                    if (maze[queue[0][0] + i][queue[0][1] + j]==1) and ((queue[0][0] + i,queue[0][1] + j) not in log):
                        #print("able",i,j)
                        queue.append((queue[0][0] + i,queue[0][1]+j))
                        log.append((queue[0][0] + i,queue[0][1]+j))
                        #print("log:",log)
                        #print("queue:",queue,":",lenth)
                    else:
                        #print("unable",i,j)
                        pass
                else:
                    #print("unable",i,j)
                    pass
            else:   
                #print("unable",i,j)
                pass
        del(queue[0])#del말고 pop 쓰기
    lenth += 1
    if queue[-1] != (N-1,M-1):
        break
print(lenth)

'''
1차시도, 오류발생
이미 방문했던 값들을 제외해야 오류가 없어질 듯

2차시도, 오류발생
이미 방문했던 값들을 제외하는 코드를 추가함
queue에 담긴 모든 값에 대한 순회가 이루어 지지 않음
'''

#솔루션: 배열 그대로 복사해서 같은지 체크