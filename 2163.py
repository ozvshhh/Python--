#초콜릿 자르기
#가능한 큰 덩어리로 자르는게 좋을듯?
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
print(M*N-1)


'''
2*2 > 3번
2*3 > 5번
3*3 > 8번
3*4 > 11번
5*3 > 14번

3*5 > 
5*3
N*M-1

(M-1) + (M*(N-1))
M - 1 + MN - M
MN - 1
'''