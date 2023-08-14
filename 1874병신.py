from time import sleep

stack = []
save = []

T = int(input())

for test_case in range(T):
    n = int(input())
    print(n)
    if len(stack) == 0:
        stack.append(n)
        print('first start')
        print('+')
        print('stack',list(stack))
        print('save',list(save))
    else:
        if stack [-1] < n:
            stack.append(n)
            print('n to stack')
            print('+')
            print('stack',list(stack))
            print('save',list(save))
        else:
            for i in range(len(stack)):
                if stack[-1] > n:
                    save.append(stack.pop())
                    print('stack to save')
                    print('-')
                    print('stack',list(stack))
                    print('save',list(save))
                else:
                    break
            stack.append(n)
            print('n to stack')
            print('+')
            print('stack',list(stack))
            print('save',list(save))
            
            for i in range(len(save)):
                stack.append(save.pop())
                print('save to stack')
                print('+')
                print('stack',list(stack))
                print('save',list(save))
            
            #print('stack',list(stack))
            #print('save',list(save))
        
'''
바닥[   ]천장
stack = 바닥[ 오름차순 ]천장
stack = [1,2,3,4]

save = 바닥 [ 내림차순 ] 천장
save [4,3,2,1]


0 - 그냥 처음은 0임
1 - 오름차순을 만족해서 바로 갖다 박는거
2 - 오름차순 만족 안해서 뺴는거
3 - ??
4 - 빼 놓은거 다시 넣는 거
'''
