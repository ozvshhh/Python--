#정사각형
import sys
input = sys.stdin.readline
N = int(input())

sqrt = [[] for i in range(N)]

for i in range(N):
    line = input()
    for j in range(N):
        sqrt[i].append(int(line[j]))
        
#print(sqrt)

#1 찾기
def findOne(maze,N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                maze[i][j] = 0
                return (i,j)
    return False


def bfs(one_idx):
    count = 1
    queue = []
    queue.append(one_idx)
    one_idx = queue[0]
    
    while True:
        global sqrt
        old_count = count
        #건전성 탐색
        searcher = [(1,0),(-1,0),(0,1),(0,-1)]
        if 0 <= one_idx[0] + 1 <N:
            pass
        else:
            searcher.remove((1,0))
        if 0<= one_idx[0] - 1 <N:
            pass
        else:
            searcher.remove((-1,0))
        if 0 <= one_idx[1] + 1 < N:
            pass
        else:
            searcher.remove((0,1))
        if 0<= one_idx[1] - 1 < N:
            pass
        else:
            searcher.remove((0,-1))
        
        #인접한 1 탐색
        for i,j in searcher:
            nx = i+one_idx[0]
            if sqrt[one_idx[0]+i][one_idx[1]+j] == 1:
                queue.append(((one_idx[0]+i),one_idx[1]+j))
                sqrt[one_idx[0]+i][one_idx[1]+j] = 0
                count += 1
        
        #print(queue)
        
        if len(queue) == 0:
            break
        else:
            queue.pop(0)
            if len(queue) == 0:
                break
            else:
                one_idx = queue[0]
            
        
    
    #탐색 군집의 1 갯수 출력
    return count 
    

count_list = []

# one_idx = findOne(sqrt,N) 
# print(one_idx)
# a = dfs(one_idx)
# print(a)
# one_idx = findOne(sqrt,N) 
# print(one_idx)
# a = dfs(one_idx)
# print(a)
# one_idx = findOne(sqrt,N) 
# print(one_idx)
# a = dfs(one_idx)
# print(a)



while True:
    try:
        one_idx = findOne(sqrt,N) 
        if one_idx == False:
            break
        #print(one_idx)
        save = bfs(one_idx)
        if save == 0:
            count_list.append(1)
            #print("break")
            
        else:
            count_list.append(save)
    except:
        break
count_list.sort()

print(len(count_list))
for i in count_list:
    print(i)
    
#라이브러리 queue 쓰기
#이중배열 탐색할때 x,y 좌표 배열 나누기
#while 조건문에 queue배열 넣으면 길이 0 되면 알아서 멈춤
#findOne 돌리다가 1 나오면 bfs 돌리기 -bfs 끝나면 findOne 이어서 돌리기
#https://www.acmicpc.net/source/share/af5841fc357e4cab923985b7f3a120ea