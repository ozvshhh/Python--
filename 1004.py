'''
어린왕자

a = 출발점을 둘러싼 원의 갯수를 센다.
b = 도착점을 둘러싼 원의 갯수를 센다.
c = 두 점을 모두 포함하고 있는 원의 갯수를 센다.

a + b - 2c 이렇게 하면 대충 나올 듯?

핵심기능:
한 점을 둘러 싼 원의 갯수를 센다!!
좌표를 반지름이 0인 원으로 간주한다.
두 원점 사이의 거리 < 반지름 -> 안에 있다!
'''

from math import sqrt
T = int(input())
way = 0

for i in range(T):
    x1, y1, x2, y2 = map(float,input().split())
    
    n = int(input())
    for i in range(n):
        x3, y3, r3 = map(float,input().split())
        
        dis_start_circle = sqrt(((x3-x1)**2) + ((y3-y1)**2))
        dis_finish_circle = sqrt(((x3-x2)**2) + ((y3-y2)**2))
        
        if (dis_start_circle <= r3) != (dis_finish_circle <= r3):
            way += 1
        else:
            continue
        
    print(way)
    way = 0