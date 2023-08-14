TMI=lambda:tuple(map(int,input().split()))
II=lambda:int(input())

'''
n 조건 10000
n*n 10억
1초 - 100만~1000만
'''

N = II()
lst = TMI()
target = II()
start = 0
end = max(lst)

while start<=end:
    
    total = 0
    mid = (start+end)//2
    
    for i in range(len(lst)):
        if lst[i]<mid:
            total += lst[i]
        else:
            total += mid
    if total <= target:
        start = mid + 1
    elif total > target:
        end = mid - 1
print(end)