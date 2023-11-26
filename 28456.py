import sys

input = sys.stdin.readline



N = int(input())
arr = []
for n in range(N):
    arr.append(list(map(int,input().split())))


C = int(input())


def one(row):
    
    arr[row][-1], arr[row][0] = arr[row][0], arr[row][-1]
    
def two():
    for i in range(N):
        for j in range(N):
            

for c in range(C):
    command = int(input())
    
    if command == 1:
        one(int(input()))
    elif command == 2:
        two()
