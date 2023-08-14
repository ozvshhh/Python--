#ATM

import sys
input = sys.stdin.readline

II=lambda:int(input())
LI=lambda:list(map(int,input().split()))

N = II()
times = LI()
main_list = []
for i in range(len(times)):
    main_list.append((i,times[i]))
    
main_list.sort(key = lambda x:x[1])
#print(main_list)

sum = 0
val = 0
for i in main_list:
    sum += i[1]
    val += sum
print(val)