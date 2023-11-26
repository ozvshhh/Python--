import sys

input = sys.stdin.readline

move = int(input())
now = 100
M = int(input())
remove_btn  = list(map(int,input().split()))

print(remove_btn)

num_list = [i for i in range(500001)]

for i in range(500001):
    for j in remove_btn:
        if num_list[i] == j:
            