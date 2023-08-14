
import sys
import math
LMI = lambda:list(map(int,input().split()))

def BS(lst,target):
    start = 0
    
    

x,y = LMI()
z = ((y/x)*100) # 승률 구하기
z = str(z)
z = z[3:8]
print(int(z))





'''
이 문제의 x의 최댓값은 무려 10억이다.
훑어봐야 할 값은 x,y 총 2가지 인 것 같다.
x,y에 이진 탐색을 돌리면
최대 2*log(2,1000000000)의 시간복잡도를 지니며
60번 이내의 연산으로 답을 산출할 수 있다.

start
end
target
값을 무엇으로 잡을 것인가?

여기서 의문점!
for문을 통해 list를 선언하면 n의 시간복잡도를 지닐까?
a = [i for i in range(1000000000)]
print(len(a))
Timed_Out이라는 결과가 나왔다 이런 식으로 선언하면 값이 너무 커진다

list를 너무 길게 선언하면 공간복잡도가 커져서 에러가 나겠지?

이 문제를 for 문을 이용해서 해결할 수 있다고 가정하자.
가정을 통해 솔루션을 찾을 수 있다.

z = math.trunc((y/x)*100)를 통해 z 값을 구한다
for 문을 이용해 x와 y에 1을 더하고
연산을 진행한다.
기존 z 값과 math.trunc(y/x*100)의 값을 비교하고
두 값이 다르다면 for문의 인자 i를 출력한다.

소수점 아래 숫자로 탐색을 돌려보면 되려나?
'''