#행렬
#행렬을 뒤집는데 필요한 연산 횟수의 최솟값
#뒤집기는 3x3으로만 가능하다.
'''
3x3 범위로 만들 수 있는 형태

0칸 3x3
111
111
111

1칸 5x5
11100
11100
11011
00111
00111

2칸 5x4 ,4x5
11100
11011
11011
00111
 
3칸 5x3, 3x5
11011
11011
11011

3칸 3x5
111
111
000
111
111

4칸 4x4
1110
1001
1001
0111
4칸 4x4
0111
1001e
1001
1110

6칸 4x3,3x4
0110
0110
0110

3인가
4인가
5인가

매트릭스 넓이를 보면
몇번 연산해야할지 보임
N-2 세로
M-2 가로

33,34,35,43,45,53,54,55 체크

'''
import sys
input = sys.stdin.readline

II=lambda:int(input())
LI=lambda:list(map(int,input().split()))

N,M = LI()
matrixes = []
sums = []


def calXOR(bin1,bin2):
    bin3 = ''
    for i in range(len(bin1)):
        if bin1[i] == bin2[i]:
            bin3 += '0'
        else:
            bin3 += '1'
    return bin3

def scan3X3(matrixes2,x,y):
    count = 0
    for i in range(x,x+3,1):
        for j in range(y,y+3,1):
            print(matrixes2[i][j]) 
    return count
            
for i in range(2):
    n = []
    for j in range(N):
        n.append(input()[0:4])
    matrixes.append(n)
print(matrixes)
print(matrixes[0][1])

matrixes2 = []
for j in range(N):
    matrixes2.append(calXOR(matrixes[0][j],matrixes[1][j]))
print(matrixes2)

count_1_in_matrixes = []
if (N<3)and(M<3):
    print(-1)
else:
    for i in range(N-2):
        for j in range(M-2):
            count_1_in_matrixes.append(scan3X3(matrixes2,i,j))
print(count_1_in_matrixes)
'''
솔루션 - 그냥 1이 보이면 냅따 찍어버리기
이건 전혀 그리디하지 않아.

3x3 범위를 스캔 -> 1이 가장 많은 것을 탐색 -> 변경 실행
요런 방식으로 하면 좋을듯.
일단은 위 방식으로 구현하고
시간초과 뜨면 다프처럼, 스캔 한 값들 배열에 저장해서, max 빼내는 방식으로 해서 단축하면 굿굿
'''
#[['0000', '0010', '0000'], ['1001', '1011', '1001']]