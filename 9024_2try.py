
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

'''
문제를 다시 풀어보자
목적은 코드를 간결하게하기!
시간복잡도 줄이기!
이거 2가지를 목표로 구상부터 다시하자

#입력되는 값
n,K,list
#출력해야 할 값
K에 가장 가까운 두 정수의 조합의 수
#사용해야 할 도구
제한시간이 2초이고
리스트의 길이가 100만이기 때문에
탐색 알고리즘을 필요로 한다.
BinarySearch or TwoPointer
(난 투포인터를 모르기에 바이너리 서치를 선택한다)

시간복잡도 유추
퀵솔트 O(NlogN)
BinarySearch O(logN)
NlogN + NlogN
NlogN이면 얼추 시간복잡도가 알맞다

list의 값 중
더해서 K값을 갖는 두 정수를 찾아야한다.

시간복잡도를 줄일 수 있는 방법:
max(n_list)*2 < K
이미 지나간 값에 대한 탐색을 해야할까?

첫번째 실행은 K값을 하나만 갖는 특수한 실행이다
그 이후의 실행에서는
두개의 K값을 갖고 탐색을 진행한다.
'''

#시간 초과가 뜬 코드
'''
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    n_list = list(map(int,input().split()))
    count = 0
    output = 0
    n_list.sort() #NlogN
    loop = 0
    while (count==1) or (count==0):
        for i in range(2):
            if loop%2 == 1:
                k += loop
            else:
                k -= loop
            count = 0
            for i in range(n):#N
                target = k - n_list[i]
                start = 0
                end = n-1
                while start <= end:#logN
                    mid = (start+end)//2
                    if n_list[mid] < target:
                        start = mid + 1
                    elif n_list[mid] > target:
                        end = mid - 1
                    else:
                        count += 1
                        break
            if count%2 == 1:
                output += (count-1)//2
            else:
                output += count//2
            if loop == 0:
                loop += 1
                break 
            else:
                loop += 1
    print(output)
    '''

#가까운 두 수이기 때문에
#가까운 정도를 활용한 수식을 쓰면
#제어문을 더 줄일 수 있다.
#두 정수의 합에 관한 제어문을 써보자
#logN 수식 안에서 연산횟수를 늘리는 것이
#N수식 안에서 연산 횟수를 늘리는 것 보다 훨씬 효과적이다!
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    n_list = list(map(int,input().split()))
    n_list.sort() #NlogN
    min = 200000000 # <-k+k 
    for j in range(n):#N
        start = j + 1
        end = n - 1
        while start <= end:#logN
            mid = (start+end)//2
            target = n_list[j] + n_list[mid]
            if target > k:
                end = mid -1
            else:
                start = mid + 1
            if (abs(k-target) < min):
                count = 1
                min = abs(k-target)
            elif (abs(k-target) == min):
                count += 1
    print(count)