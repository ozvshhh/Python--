import sys
from math import sqrt
input = sys.stdin.readline
II=lambda:int(input())

n = II()

start = 0
end = int(sqrt(n)+1)

def BinarySearch(i):
    global start
    global end
    while start <= end:
        mid = (start+end)//2
        if mid**2 < i:
            start = mid+1
        elif mid**2 > i:
            end = mid - 1
        else:
            return mid
    return mid

print(BinarySearch(n))
    
'''
while start <= end:
    mid = (start+end)//2
    if mid**2 < n:
        start = mid+1
    elif mid**2 > n:
        end = mid -1
    else:
        print(start)
        checker = True
if checker == True:
    pass
else:
    print(start)
    
1. 출력초과가 떴다.
출력초과 뜬 이유를 짐작해보자면
print()가 2번 실행된듯
그래서 if 문 추가했는데
안고쳐짐;;

2. 실행문을 함수로 바꾸고
아래에서 호출했는데 오류가 뜸.
변수를 불러올 수 없다는 오류였음.
파이썬에서 함수는 전역 함수를 불러올 수 없는 것인가?
A.(가온누리 회장님 신재희)
파이썬 함수에서 전역변수를 불러오려면
global variation 이 구문을 통해
전역변수를 불러와야한다.
_감사합니다잉

3.제출해보니 99퍼에서 오류걸림
예외 케이스를 찾기위해
#input
0
#output
0

#input
1
#output
1
#Recived output #오류가 나버림
0

return start 구문을
return mid 구문으로 고치니
위의 테스트 케이스에서의 오류가 고쳐짐
'''