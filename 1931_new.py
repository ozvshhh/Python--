import sys
input = sys.stdin.readline

II = lambda :int(input())
LI = lambda :list(map(int,input().split()))

time_table = []

for i in range(II()):
    start,end = LI()
    time_table.append((start,end))
time_table.sort(key=lambda x:x[0])
time_table.sort(key=lambda x:x[1])

#print(time_table)

max = 0
count = 0
for start,end in time_table:
    if start >= max:
        count += 1
        max = end
print(count)