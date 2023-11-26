# 꿀 따기

N = int(input())
honeys = list(map(int,input().split()))
save = [max(honeys)]+[0]*100000
max_honey = 0
# print(len(honeys))
# print(len(save))
'''
로직을 생각해보자
n= 100,000
제한시간 1초
시간복잡도 NlogN 나와야한다.
꿀통의 위치 N
구간합 log N


#벌벌 구간합
#벌꿀 구간합
'''

    

'''
구간 합의
3가지 경우의 수 다른 연산

벌1 꿀 벌2
벌1 ~ 꿀, 꿀 ~ 벌2

꿀 벌1 벌2
꿀 ~ 벌1, 2*(벌1 ~ 벌2)

벌1 벌2 꿀
2*(벌1 ~ 벌2), 벌2 ~ 꿀
'''