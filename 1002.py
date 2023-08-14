#터렛
#두 원의 교점의 수 구하기
#두 원의 교점의 경우의 수
#1. 두 점에서 만난다.
#2. 한 점에서 만난다.(외접) : 거리 > 반지름의 합
#3. 한 점에서 만난다.(내접) : 거리 < 반지름의 합
#4. 모든 점에서 만난다.(합동) : 거리 == 반지름의 합
#5. 어떤 점에서도 만나지 않는다.(0) : 
import math 
T = int(input())


for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(float,input().split())
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    
    
    if (((r1+r2)<distance)) or (abs(r1-r2)>distance) :
        print(0)
        
    elif (((r1+r2) == distance) or (abs(r1-r2) == distance)) and (distance != 0): 
        print(1)        
    
    elif (((r1+r2) > distance) or (abs(r1-r2) < distance)) and (distance != 0):
        print(2)
    
    else:
        print(-1)