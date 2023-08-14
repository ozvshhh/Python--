import sys
input = sys.stdin.readline

LI = lambda:list(map(int,input().split()))

N,M = LI()

mtrx1 = []
mtrx2 = []

def mtrx1_reverse(mtrx):
    for x in range(N):
        for y in range(M):
            if mtrx[x][y] == 0:
                mtrx[x][y] = 1
            else:
                mtrx[x][y] = 0
    return mtrx

for i in range(N):
    line = list(input()[0:M])
    line = list(map(int,line))
    mtrx1.append(line)

for i in range(N):
    line = list(input()[0:M])
    line = list(map(int,line))
    mtrx2.append(line)

#print(mtrx1)
#print(mtrx2)


#N,M이 3이상일 때에만 작동
count = 0
if N >= 3 and M >=3:
    for i in range(N-2):
        for j in range(M-2):
            #다르면
            if mtrx1[i][j] != mtrx2[i][j]:
                #mtrx1을 뒤집는다.
                count += 1
                for x in range(i,i+3,1):
                    for y in range(j,j+3,1):
                        if mtrx1[x][y] == 0:
                            mtrx1[x][y] = 1
                        else:
                            mtrx1[x][y] = 0

    if mtrx1 == mtrx2: 
        print(count)
    else:
        print(-1)
else:
    #예외처리
    if mtrx1 == mtrx2:
        print(0)
    # elif mtrx1_reverse(mtrx1) == mtrx2:
    #     print(1)
    else:
        print(-1)

