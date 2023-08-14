#2138 전구와 스위치

import sys
input = sys.stdin.readline

II = lambda:int(input())
T = II()
a = input()
b = input()

first = []
second = []

for i in range(T):
    first.append(int(a[i]))
    second.append(int(b[i]))

#print(first)
#print(second)

count = 0
if T >= 3:
    #최초의 2뒤집기
    if first[0] != second[0]:
        count += 1
        for i in range(2):
            if first[i] == 0:
                first[i] = 1
            else:
                first[i] = 0
    
    #최후의 2뒤집기    
    if first[T-1] != second[T-1]:
        count += 1
        for i in range(T-1,T-3,-1):
            if first[i] == 0:
                first[i] = 1
            else:
                first[i] = 0

    if T >= 5:
        # T-2 만큼 3뒤집기
        for k in range(1,T-1,1):
            if first[k] != second[k]:
                count += 1
                for i in range(k,k+3):
                    if first[i] == 0:
                        first[i] = 1
                    else:
                        first[i] = 0

if first == second:
    print(count)
else:
    print(-1)
'''
양 끝 값을 뒤집을 때에는
2개만 뒤집힌다. 이것은 언제나 적용된다.
뒤집는 순서는 상관없다.
중요한건 뒤집는 횟수이다.

탐색을 조진다.
탐색 index가 0 또는 
'''