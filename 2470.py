'''
sort NlogN

1 2 3 4 5 N

def calDef(i,m):
    return m-i;
'''

import sys

input = sys.stdin.readline

n = int(input())
nums = sorted(map(int, input().split()))


def binSearch(target, start):
    global min_diff , a, b
    left = start
    right = len(nums)

    while left + 1 < right:

        mid = (left + right) // 2

        if nums[mid]+target <= 0:
            left = mid
        else:
            right = mid

        if min_diff > abs(nums[mid]+target):
            min_diff = abs(nums[mid]+target)
            a, b = target , nums[mid]
    return left

min_diff = 2_000_000_001

a,b=-1,-1
for i in range(len(nums)-1):
    j = binSearch(nums[i], i)
print(a,b)

