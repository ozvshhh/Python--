import sys
from collections import deque
# import math
input = sys.stdin.readline

def fiveRound(num):
  if num - int(num) >= 0.5:
    return int(num+1)
  else:
    return int(num)

N = int(input())
point = deque()
min = 31
max = 0
for n in range(N):
  level = int(input())
  point.append(level)

point = deque(sorted(point))
out = fiveRound(N*(0.15))
for i in range(out):
  point.popleft()
  point.pop()

if N==0:
  print(0)
else:
  # if out==0:
  #   print(math.ceil(sum(point)/N))
  # else:
    print(fiveRound(sum(point)/(N-(out*2))))  