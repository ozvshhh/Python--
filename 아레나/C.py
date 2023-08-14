#숫자를 발란스 있게 만들어라
import sys
from heapq import *
input = sys.stdin.readline

n = int(input())

nums = list(map(int,input().split()))

heapify(nums)
#print(nums)

def calMinMax(list1):
    return(max(list1)-min(list1))

def beDouble():
    heappush(nums,heappop(nums)*2)
    
diff = calMinMax(nums)

while True:
    beDouble()
    new_diff = calMinMax(nums)
    print("new_diff",new_diff)
    print("diff",diff)
    if new_diff <= diff:
        diff = new_diff
    else:
        break
beDouble()
print(calMinMax(nums))
#print(nums)
#print(diff)
