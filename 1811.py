#마인크래프트
#땅고르기

'''
세로 N
가로 M
집터 왼쪽 위는 (0,0)
평평한 땅이 목표다!

좌표(i,j)의 가장 윗 블록을 인벤토리에 넣기
'''

import random

array = [random.randint(-10**8, 10**8) for _ in range(1000000)]
for i in range(len(array)):
    print(array[i],end='',sep=' ')