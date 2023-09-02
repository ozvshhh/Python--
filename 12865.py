import sys

input = sys.stdin.readline

N,K = map(int,input().split())

items = []

for n in range(N):
    items.append(tuple(map(int,input().split())))

print(items)


'''
i,j 물건이 i개 있을 때 물건이 j 라고 하면 가치의 최댓 값
'''