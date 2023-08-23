#두 용액
#투포인터로도 풀 수 있고, 이진탐색으로도 풀 수 있을듯?
'''
sort NlogN

1 2 3 4 5

def calDef(i,m):
    return m-i;
'''

import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(map(int,input().split()))


def binSearch(target,arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left+right)//2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    answer = arr[mid]
    min = abs(target - arr[mid])
    #print("answer",arr[mid])
    if mid-1 >=0:
        if min > target-arr[mid-1]:
            answer = arr[mid-1]
    
    if mid+1 < len(arr):
        if min > arr[mid+1] - target:
            answer = arr[mid+1]
    return answer
 
    #경계선 기준 앞뒤를 생각해보기.


min_diff = 2000000000
mins = [0,0]
for i in range(len(nums)-2):
    j = binSearch(nums[i]*-1,nums[i+1:])    
    #rint(i,nums[i],j)
    #print(nums[i]+j)
    if abs(nums[i]+j) < min_diff:
        #print("#",i,nums[i],j)
        mins = [nums[i], j]
        min_diff = abs(nums[i]+j)
print(min(mins),max(mins))


'''
테스트 케이스를 잘 분석해보자
!정렬
-3 -2 1 (경계) 4 5
 F  F F        T T
3이상인가?

1 2 (경계) 3 4 5
F F        T T T

-3을 기준으로 삼는다.
3이 배열 속 어느 위치에 존재할지 판단한다.
1와 4사이가 3의 위치가 된다
1와 4를 비교하고 같으면 작거나 같은 수를
-3과 함께 출력한다.

값을 순회할 때 본인값 빼고 돌아야됨..
4번 테스트케이스에서, 0 0이 출력되는데.
0 값에 대해 이진탐색을 진행하는 배열에는 0 값이 제외되어야한다.
-> 시간초과 떳음..
정렬 NlogN
순회 N
이렇게 라서
N**2 logN 이라 그런듯..
N 하나만 없애고 싶다;;
'''