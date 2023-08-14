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
    end = L[-1]
    while start <= end:
        mid = (start+end)//2
        if mid < value:
            start = mid + 1
        elif mid > value:
            end = mid - 1
        else:
            return(1)
    return(0)

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

'''