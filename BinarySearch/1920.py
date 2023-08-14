import sys
input = sys.stdin.readline
LMI=lambda:list(map(int,input().split()))
II=lambda:int(input())

n1 = II()
lst1 = sorted(LMI())
n2 = II()
lst2 = LMI()


def BinarySeaerch(L,value):
    start = 0
    end = len(L)-1
    if len(L) == 1:#배열의 크기가 1인경우
        if L[i] == value:
            return 1
        else:
            return 0
    else:#배열의 크기가 1이 아니라면 이진탐색 시작
        while start <= end:
            mid = (start+end)//2
            if L[mid] < value:
                start = mid + 1
            elif L[mid] > value:
                end = mid - 1
            else:
                return 1
        return 0

for i in range(len(lst2)):
    print(BinarySeaerch(lst1,lst2[i]))
'''
시간초과가 뜬다;;
시간 복잡도를 계산해보자.
1. max(L) +n번
2. BinarySearch log2 n
3. for *n번
((log2 n)+n)*n 의 시간복잡도를 가진다.
n 값이 최대 10만이니
10억 번의 계산을 필요로 한다;;
근데 1초당 - 1억번 계산을 수행하니
이 방법은 문제가 있는 것 같다.
그래서 pypy3로 돌리니깐 어케든 답은 나오는 느낌이다
log(2,100000) = 16.6번의 계산을 필요로 한다

1.배열의 크기가 1인 경우 오류가 나는 것 같아서
if(len(L) == 1):
else:
BinarySearch
구문을 넣어 주었다

2.리스트에 들어오는 정수 값의 범위가 -2**31 ~ -2**31
범위라는 것을 고려하지 않고 start의 초기값을 1로 주었던 코드를
sorted(L)
start = L[0] 
end = L[-1]
이렇게 코드를 고쳤다

3.list의 값이 음수인 경우를 제대로 고려하지 않은 것 같아
#input
5
-7 -4 3 8 5
5
-7 1 2 3 5
#Expected output
1
0
0
1
1
#Recive Output
1
1
1
1
1
테스트 케이스를 추가하였다
모두 1로 나타나는 오류가 떴다 BinarySearch 함수의 작동 과정을 분석해보자
종이에 케이스들을 손으로 적어가다보니 오류를 알 수 있었다.
start, end, mid 값들은 인덱스에 대한 값인데
인덱스 값을 갖고 이진탐색을 돌려서 오류가 떳다.
start = 0
end = len(L) - 1
mid > target 코드를 L[mid] > target
mid < target 코드를 L[mid] < target 
이렇게 코드를 고쳤더니 문제가 해결되었다.
'''