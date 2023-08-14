import sys
input = sys.stdin.readline
from itertools import combinations

N,M = map(int,input().split())
cards = list(map(int,input().split()))
Min = 1000000000
nums = []
for card in combinations(cards,3):
    diff = M-sum(card)
    if diff >= 0:
        if diff <= Min:
            nums = sum(card)
            Min = diff
    else:
        continue
print(nums)