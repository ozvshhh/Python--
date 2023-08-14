cups = [1,0,0]
M = int(input())

for i in range(M):
    x, y = map(int,input().split())
    cups[x-1],cups[y-1] = cups[y-1],cups[x-1]
print(cups.index(1)+1)