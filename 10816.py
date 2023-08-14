import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int,input().split()))
cards.sort()
M = int(input())
find_list = list(map(int,input().split()))

for i in find_list:
    def binSearch(list1,target):
        start = 0
        end = len(list1)-1
        while start <= end:
            mid = (start+end)//2
            if target < list1[mid]:
                end = mid - 1
            elif target > list1[mid]:
                start = mid + 1
        return start
    