import sys
input = sys.stdin. readline


#입력 및 선언
N = int(input())
relation = [[]for _ in range(N+1)]
start, end = map(int,input().split())

for _ in range(int(input())):
    x,y = map(int,input().split())
    relation[x].append(y)
    relation[y].append(x)
stack = []

#dfs 함수
def dfs():
    if start == end:
        return 0
    
    #초기값 설정
    distance = 0
    stack.append(start)
    visted = [False for _ in range(N+1)]
    
    
    while stack:
        target = stack.pop()
        visted[target] = True
        distance += 1
        backer = True # 끝까지 탐색해도 안나올 경우 거리 -1을 판단하기 위한 변수
        for num in relation[target]:
            if not visted[num]:
                backer = False
                if num == end:
                    return (distance)
                else:
                    stack.append(num)
                    visted[num] = True
            else:
                continue
        if backer == True:
                    distance -= 1
                
    return (-1)

print(dfs())

'''
그래프로 생각하고 dfs로 최단거리 조지기
dfs로 최단거리 하는 법
탐색을 했다면, 길이 +1
더이상 탐색할 공간이 없다면
길이 -1을 하고 다시 탐색 시작
[[1,4],[2,3],[7,8,9],[],[5,6],[],[],[],[],[]]
''' 