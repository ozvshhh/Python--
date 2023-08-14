'''
이진탐색
n=1 k=2
n=2 k=3,4
n=3 k=4,6
n=4 k=5,8,9
n=5 k=6,10,12
n=6 k=7,12,15,16
n=7 k=8,14,18,20,
n=8 k=9,16,21,24,25
n=9  k=10,18,24,28,30
n=10 k=11,27,32,35,36

k 값은 계차수열로 나온다
n에 대한 k값의 수열(계차수열)은
계차수열의 i 번째 항
i의 최댓값은

if n%2 == 0:
    max = n//2
else:
    max = (n//2) + 1
    
i=0:((max)+1)^2 - ((n//2)-i)^2 <- 초항
i=max:((max)+1)^2 - ((n//2)-i)^2 <- 말항


if n%2 == 0:
    x_max = n//2
else:
    x_max = (n//2) + 1
i번째항 일반화 식
if (1 <= i <= x_max): <-(0 <= i-1 <= x_max-1)
    (x_max+1)^2 - (x_max-(i-1))^2

초항, 말항을 정한다
중항을 찍는다
내가 서치할 값을 중항 과 비교한다
크고 작음에 따라서 초항 말항을 다시 정의하고
서치할 값과 중항을 비교한다
위 과정(이진탐색)을 반복하여
중항과 서치할 값이 같으면 True를
중항과 서치할 값이 다르면 False를 출력한다
'''
import sys
input = sys.stdin.readline

n, target = map(int,input().split())
state = 'even' #'even' or 'odd'

if n%2 == 0:
    x_max = n//2
    state = 'even'
else:
    x_max = (n//2)+1
    state = 'odd'

def arithmetic_sequence(max,i):
    if state == 'even':
        answer = (max+1)**2 - (max-i)**2
        return answer
    elif state == 'odd':
        answer = (max+1)**2 - (max-(i-1))**2 - i
        return answer
    else:
        return 'error'

def BS(max):
    start = 0
    end = max+1
    while start <= end:
        mid = (start+end)//2
        #print('value',arithmetic_sequence(max,mid))
        #print('target',target)
        if arithmetic_sequence(max,mid) < target:
            start = mid + 1
        elif arithmetic_sequence(max,mid) > target:
            end = mid - 1
        else:
            return 'YES'
    return 'NO'

print(BS(x_max))