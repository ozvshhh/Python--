'''
5를 입력 받았다.
1
3
5
7
9
7
5

공간이 9칸 필요하다
별의 수 : 2*i - 1
전체 공간의 수 : 2*n - 1
2n- 2i
전체공간의 수 - 별의 수 / 2 = 한쪽 빈공간의 수
출력(한쪽 빈 공간,별의수,한쪽빈공간, sep='')
위 과정을 n번 반복
'''
n = int(input())

for i in range(n):
    print(" "*(((2*n)-(2*(i+1)))//2),"*"*((2*(i+1))-1),sep ='')

for i in range(n-2,-1,-1):
    print(" "*(((2*n)-(2*(i+1)))//2),"*"*((2*(i+1))-1),sep ='')