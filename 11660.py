import sys
input = sys.stdin.readline

N,M = map(int,input().split())
poses = []
table = []

for n in range(N):
    table.append(list(map(int,input().split())))

for m in range(M):
    poses.append(list(map(int,input().split())))
 
#가로 구간합 배열 생성
sum_table = [[sum(table[i][:j+1]) for j in range(len(table[0]))] for i in range(len(table))]

#세로 구간합 해주기 
for j in range(len(sum_table[0])):
    for i in range(len(sum_table)-1):
        sum_table[i+1][j] += sum_table[i][j] 

print(sum_table)
for pos1_x,pos1_y,pos2_x,pos2_y in poses:
    print(sum_table[pos2_x-1][pos2_y-1] - sum_table[pos1_x-1][pos2_y-1] - sum_table[pos2_x-1][pos1_y-1] + sum_table[pos1_x-1][pos1_y-1])
    
[[0,0,0,0,0]
 [0,1, 3, 6, 10], 
 [0,3, 8, 15, 24], 
 [0,6, 15, 27, 42], 
 [0,10, 24, 42, 64]]