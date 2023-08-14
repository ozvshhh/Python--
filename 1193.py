#좌표 -> 번째 수
#번째 수 -> 좌표
#로 반환해주는 함수(기능) 구현하기
#분수를 좌표로 보자

#(1,1) (1,2)
#(2,1) (2,2)
#이차원 배열임을 알 수 있다

#대각선으로 번호를 메긴다.
#대각선 값 끼리는 좌표의 합이 같다

#X+1은 좌표의 합이다
#(1,X) 대각 선 첫 대가리의 좌표이다
#(1,X)는 몇번째 값일까?
#X=1 -> 첫번째
#X=2 -> 1+2
#X=3 -> 1+2+3
#대각선 대가리의 좌표는 1~X까지의 합이다.
#대가리의 좌표 ( 1 , (X(X+1))/2 )
#(1+n,X-n) 은 대각선 n번째 값의 좌표이다
x = float(input())
i = 0.0
while (((i*(i+1.0))/2.0) < x):
    i += 1
#print(i)#대가리값의 좌표를 구했다

n = (((i*(i+1))/2)-(x))

#지그재그 여부 판단
if i%2 == 0:
    print(f'{int(i-n)}/{int(1+n)}')
else:
    print(f'{int(1+n)}/{int(i-n)}')

