import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))

# + - * int(/) 순서이다
# 0 1 2 3      이렇게 드가자
operator = list(map(int,input().split()))
Min = 1000000001
Max = -1000000001

operator_tools = []
for i in range(len(operator)):
    for j in range(operator[i]):
        operator_tools.append(i)

#print(operator_tools)

for i in permutations(operator_tools,len(operator_tools)):
    sum = numbers[0]
    for j in range(len(i)):
        #print(i,j)
        #print(numbers[j+1])
        
        if i[j] == 0:
            sum += numbers[j+1]
        if i[j] == 1:
            sum -= numbers[j+1]
        if i[j] == 2:
            sum *= numbers[j+1]
        if i[j] == 3:   
            sum = int(sum/numbers[j+1])
    if sum < Min:
        Min = sum
    if sum > Max:
        Max =sum

print(Max)
print(Min)