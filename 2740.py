N ,M = map(int,input().split())

matrix_A = []
matrix_B = []

for i in range(N):
    matrix_A.append(list(map(int,input().split())))

M ,K = map(int,input().split())
for i in range(M):
    matrix_B.append(list(map(int,input().split())))

# print(matrix_A)
# print(matrix_B)

matrix_C = [[0 for _ in range(K)]for _ in range(N)]

#행렬곱_세로 가로
for n in range(N):
    for k in range(K):
        for m in range(M):
            matrix_C[n][k]  += matrix_A[n][m]*matrix_B[m][k]

for c_line in matrix_C:
    for i in c_line:
        print(i,end=" ")
    print()