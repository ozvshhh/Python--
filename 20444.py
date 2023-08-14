#색종이와 쿼리

'''
직사각형 색종이 조각
n과 k가 입력된다
정확히  n번의 가위질로
k개의 색종이 조각을 만들 수 있으면 yes 아니면 no 를 출력해라
'''

import sys
import math
input = sys.stdin.readline


n,k = map(float,input().split())

if (n**2)-4*(k-n-1) > 0:
    
    root = math.sqrt((n**2)-4*(k-n-1))
    key1 = n + root
    key2 = n - root

    if(root>=0):
        if int(key1/2)==(key1/2) and int(key2/2)==(key2/2):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('YES ')
