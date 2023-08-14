white_paper = [[0 for i in range(100)] for i in range(100)]
count = 0
N = int(input())


for i in range(N):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            white_paper[x+i][y+j] = 1
for i in range(100):
    count += white_paper[i].count(1)        
print(count)

# 처음 짰던 코드.
# 넓이를 다 덮어야 하는데 가로 세로만 1로 바꾸는 오류가 있다
# for i in range(N):
#     x, y = map(int,input().split())
#     for i in range(10):
#         white_paper[x+i][y] = 1
#         white_paper[x][y+i] = 1
# for i in range(100):
#     count += white_paper[i].count(1)
