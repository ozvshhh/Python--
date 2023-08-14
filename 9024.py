import time
import sys
from math import sqrt
input = sys.stdin.readline
II=lambda:int(input())
LIM=lambda:list(map(int,input().split()))

def binaryIndexSearchCounter(arr):
    global K
    count_box = []
    for i in arr:#배열의 값 만큼 반복
        count = 0 #두 정수의 조합의 수를 저장하는 변수
        target = K - arr[i] #이진탐색으로 원본배열에서 찾을 값
        start = 0 #인덱스로 이진탐색이니 start =0
        end = len(arr)-1 #인덱스 땜에 len(arr)-1
        loop_checker = 1 #몇번 반복했는지 판단함 target값을 조정하기 위해 선언한 함수
        while ((count==1)or(count==0)):#자기를 포함한 (k,k)순서쌍이 나오거나 어떤 값도 도출되지 않으면 재실행
            while start<=end:#이진탐색문
                mid = (start+end)//2
                if arr[mid] < target:
                    start = mid+1
                elif arr[mid] > target:
                    end = mid-1
                else:
                    count += 1 #탐색이 되는경우 count를 + 1
                    break # 이진탐색 while문 종료
            if loop_checker%2 == 1: #정수 K 에 가장 가까운 두 정수의 조합의 수를 출력한다.
                target -= loop_checker #target에 -1 +2 -3 +4 -5 +6 이런식으로 해서 가까운 정수를 구해 비교한다
                loop_checker += 1
                print(loop_checker,':',count,':',target)
            else:
                target += loop_checker
                loop_checker += 1
                print(loop_checker,':',count,':',target)
        count_box.append(count)#count의 값을 한번에 출력하고 싶으니 배열에 넣는다
    return(count_box)#출력

for i in range(II()):
    n,K = LIM()
    n_list = sorted(LIM())
    print(binaryIndexSearchCounter(n_list))

'''
for i in range(II()):
    n,K = LIM()
    n_list = sorted(LIM())
    count = 0
    for j in range(len(n_list)):
        target = K - n_list[i]
        count += binaryIndexSearchCounter(n_list,target)
        print(count)
    print(count)
'''

'''
시간복잡도 계산
제한시간 1초 - 약 1억번 연산가능
n값 1,000,000
lon(2,n) = 19.9
t*n*log(2,n) 의 시간 복잡도를 가지면 대충 될 듯?
근데 이정도 시간복잡도를 가지면 t 값이 10 이하여야 됨..
근데 또 이진탐색 while문 돌리다보면 log(2,n) 보다 적게 나올 수 도 있을 듯?

n_lsit : -7 9 2 -4 12 1 5 -3 -2 0
sorted()
n_list : -7 -4 -3 -2 0 1 2 5 9 12
더해서 8이 되는 순서쌍(oredered pair)의 갯수를 구해라.
(12, -4)

1.이진탐색을 해야하는 상황에서
함수의 인자에 list 값을 넣어야 할 때
list 값을 함수 밖에서 sort해주는 것이 좋은 표현일까?
list를 인자로 받아서 함수 안에서 sort 해주는 게 좋은 표현일까?

함수에 인자로 넣을 때 타입이 명시되어 있지 않아 밖에서 sort를 해주는게 더 좋은 표현처럼 보인다..

핵심 코드를 짯는데 오류를 내포하고 있다.
`K 에 가장 가까운 두 정수의 조합의 수를 출력한다.`이 조건을 고려하지 않아 생긴 문제였다.
K에 가장 가까운?
이진탐색에서 알맞은 순서 쌍이 없다면
target -= 1을 하고 다시 실행하면 되려나?

너무 머리가 아프다.
그냥 함수에 값을 넣으면
중복을 검사할 수 있게 해야겠다
함수를 수정 하자
F5. 다 지우고 다시 설계해보자
'''

'''
출력해야 할 것 -> 합해서 최대값이 되는 서로 다른 순서쌍의 갯수
사용해야 할 도구 -> 존재 여부를 확인하기 위한 이진탐색
                   순서쌍의 갯수를 세어줄 변수
전체적인 구조:
1.시작최댓값(K)와 숫자로이루어진배열(N)을 입력받는다.
2.이진탐색을 이용해 최대값이 되는 서로 다른 순서쌍의 존재 여부를 확인해본다.
    2.1.서로다른 순서쌍이 없다면 K값에 +-1을 주고 (2.0)을 다시 실행한다.
    2.2 서로다른 순서쌍이 없다 +-2 탐색 시작
    .
    .
    .

'''
'''
코드를 새로 짜고 있다..
살려줘..
이번 주말 이 문제 때문에 다 날아갈 듯?
'''