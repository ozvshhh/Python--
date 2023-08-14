N,M = map(int,input().split())
matrix1=[]
matrix2=[]

for i in range(N):
    matrix1.append('')
    matrix2.append('')
    
for i in range(N):
    matrix1[i] = list(map(int,input().split()))
for i in range(N):
    matrix2[i] = list(map(int,input().split()))

for i in range(N):
    for j in range(M):
        print(matrix1[i][j]+matrix2[i][j],end=' ')
    print()