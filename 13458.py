
#총감독관 오직 한명
#부감독관 여러 명
#응시자 수 A
# 1 부감독관 - C명 , 총감독관은 B명
#총감은 한 명, 부관은 여러명


N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())

count = 0
for i in range(len(A)):
    if A[i] - B > 0:
        count += 1
        if A[i]//B
    else:
        continue