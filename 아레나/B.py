import sys
list1 = []
num = ['1','2','3','4','5','6','7','8','9','0']
pos_type = [0,0,0]
for i in range(3):
    n = input()
    for k in num:
        if k in n:
            pos_type[i] = 1
            break
    list1.append(n)

for i in range(3):
    if pos_type[i] == 1:
        list1[i] = int(list1[i])
        if i == 0:
            list1[1] = list1[i]+1
            list1[2] = list1[i]+2
        if i == 1:
            list1[0] = list1[i]-1
            list1[2] = list1[i]+1
        if i == 2:
            list1[0] = list1[i]-2
            list1[1] = list1[i]-1

answer = list1[2]+1

def aaa(answer):
    if answer%3 == 0 and answer%5 == 0:
        print('FizzBuzz')
        return
    if answer%3 == 0:
        print('Fizz')
        return
    if answer%5 == 0:
        print('Buzz')
        return
    return print(answer)

aaa(answer)