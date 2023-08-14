#timed over

import sys
input = sys.stdin.readline
II = lambda:int(input())
LMI = lambda:list(map(int,input().split()))


def BS(lst,target):
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start+end)//2
        if lst[mid] < target:
            start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            return 1
    return 0

for i in range(II()): 

    n, k = LMI()
    n_list = sorted(LMI())
    count = 0
    two_track = False
    sum_count = 0

    while (count==0)or(count==1):
        loop_checker = 1
        #print('k',k)
        if two_track == False:
            #한번 만 돌아라
            count = 0
            for i in range(len(n_list)):
                target = k - n_list[i]
                count += BS(n_list,target)
                #print(BS(n_list,target))
            #print('count',count)
            
            if (count%2 == 1) and (count != 1):
                #print('c',count)
                print((count-1)//2)
                #print('way1')
            elif (count%2 == 0)and(count != 0):
                print(count//2)
                #print('way2')
                
            elif (count == 1) or (count == 0):
                two_track = True
                if loop_checker%2 == 1:
                    k += loop_checker
                    loop_checker += 1
                elif loop_checker%2 == 0:
                    k -= loop_checker
                    loop_checker += 1
        
        elif two_track == True:
            #print('two_tracking_on')
            #print('k_value',k)
            
            sum_count = 0
            #두번 돌고 합 구해라
            count = 0
            for i in range(len(n_list)):
                target = k - n_list[i]
                count += BS(n_list,target)
                #print(BS(n_list,target))
            if (count%2 == 1) and (count != 1):
                #print('c',count)
                sum_count += ((count-1)//2)
                #print('sum',sum_count)
                #print('way1')
            elif (count%2 == 0)and(count != 0):
                sum_count += (count//2)
                #print('sum',sum_count)
                #print('way2')
            if loop_checker%2 == 1:
                k += loop_checker
                loop_checker += 1
            elif loop_checker%2 == 0:
                k -= loop_checker
                loop_checker += 1
                
            count = 0
            for i in range(len(n_list)):
                target = k - n_list[i]
                count += BS(n_list,target)
                #print(BS(n_list,target))
            if (count%2 == 1) and (count != 1):
                #print('c',count)
                sum_count += ((count-1)//2)
                #print('sum',sum_count)
                #print('way1')
            elif (count%2 == 0)and(count != 0):
                sum_count += (count//2)
                #print('sum',sum_count)
                #print('way2')
            
            if loop_checker%2 == 1:
                k += loop_checker
                loop_checker += 1
            elif loop_checker%2 == 0:
                k -= loop_checker
                loop_checker += 1
    
    if sum_count == 0:
        pass
    else:
        print(sum_count)

    


'''
10 8
-7 9 2 -4 12 1 5 -3 -2 0
-7 -4 -3 -2 0 1 2 5 9 12 - sorted
target = 8 - (-7) = 15 -> 0
target = 8 - (-4) = 12 -> 1
target = 8 - (-3) = 11 -> 0
target = 8 - (-2) = 10 -> 0
target = 8 - 0 = 8 -> 0
target = 8 - 1 = 7 -> 0
target = 8 - 2 = 6 -> 0
target = 8 - 5 = 3 -> 0
target = 8 - 9 = -1 -> 0
target = 8 - 12 = -4 -> 1
'''

'''
k = 5
-7 9 2 -4 12 1 5 -3 -2 0
-7 -4 -3 -2 0 1 2 5 9 12

taget = 5 - (-7) = 12 -> 1
taget = 5 - (-4) = 9 -> 1
taget = 5 - (-3) = 8 -> 0
taget = 5 - (-2) = 7 -> 0
taget = 5 - 0 = 5 -> 1
taget = 5 - 1 = 4 -> 0
taget = 5 - 2 = 3 -> 0
taget = 5 - 5 = 0 -> 1
taget = 5 - 9 = -4 -> 1
taget = 5 - 12 = -7 -> 1

안풀리는 이유를 찾았다.
더해서 k 값을 가지는 순서쌍이 없다면
더해서 k에 가까운 값을 가지는 두 정수에 대한 순서쌍을 출력해야한다.
k의 결과가 0 이면 (k+1),(k-1)일 때의 count를 도출하고,
그마저 없다면 k+2,k-2 이런식으로 진행해야한다.

처음에 한번만 돌려서 값을 출력하고
안되면 k값 바꿔서 2번 돌리고 그 합을 출력해


'''


'''
for i in range(len(n_list)):
    target = k - n_list[i]
    count += BS(n_list,target)#더해서 k가 되는 수가 있으면 갯수 세고 없으면 세지마

if count == 0: #만약 결과값이 0 이라면 k 값 바꾸고 다시 해
    k -= 1
    target = k = n_list[i]
    count += BS(n_list,target)

#결과 출력
if count%2 == 1: #항의 갯수가 홀수이면(k,k)항을 포함하고 있으니 -1연산
    print((count-1)//2)
else:
    print(count//2)
'''

'''
구해야할 것.
합해서 K가 되는 순서쌍.
근데 정렬했으면 절반만 구해도 되는거 아님?

i + min(n_list) < k + min(n_list)
'''