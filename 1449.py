#수리공 항승

import sys
input = sys.stdin.readline

N, L = map(int,input().split())

fluid_points = sorted((map(int,input().split())))
count = 1
start, *fluid_points = fluid_points
for point in fluid_points:
    d = point - start
    
    if d+1 > L:
        count += 1
        start = point
print(count)

