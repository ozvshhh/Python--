import sys
input = sys.stdin.readline
import math

II=lambda:int(input())
LI=lambda:list(map(int,input().split()))
time_tables = []
count_tables = []


n = II()
for i in range(n):
    start, end = LI()
    #시작시간과 걸린시간을 리스트에 튜플타입으로 저장
    time_tables.append((start,end))

time_tables.sort(key=lambda x:x[0])
time_tables.sort(key=lambda x:x[1])

print(time_tables)

#카운트의 시작값 결정하기
'''
시작과 동시에 끝나는 회의가 있을 경우 0 +1
시작과 동시에 끝나는 회의가 없을 경우 1
'''
count = 0
check1 = False
for i in time_tables:
    if i[0] == i[1]:
        check1 = True
        count += 1


if count == len(time_tables):
    pass
else:
    count += 1

#꼬이는 경우의수
#시작과 동시에 끝나는 회의만 있을 때랑
#시작과 동시에 끝나는 회의와 일반적회의가 함께 있을 때에
#코드가 꼬임.

max = time_tables[0][1]
#print('max:',max)

super_max = time_tables[-1][-1]
#print(super_max,'super')
while max < super_max:
    check = False
    for i in range(len(time_tables)):
#        print(time_tables[i][0],max)
        if time_tables[i][0] == max:
            max = time_tables[i][1]
#            print('max:',max)
            count += 1
            check = True
            break
        else:
            continue
    if check == True:
        pass
    else:
        max += 1
#    print('super:',super_max,'max:',max)
print(count)

#엔드 값이 큰 것 부터 역추적
#아 역추적 머리아픔 그냥 추적할거임





    
#모든 값에 대하여 탐색 진행 -> 시간초과
# for i in range(n):
#     count = 0
#     save = time_tables[i][1]
#     count += 1
#     try:
#         while True:
#             save = time_tables[save][1]
#             count += 1 
#     except:
#         count_tables.append(count)
# print(max(count_tables))

#어떻게 하면 그리디하게 할 수 있을까?
'''
눈 앞에 있는 값 중에서 가장 효과적인 녀석을 선택하자
'''
