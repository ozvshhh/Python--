'''
(랑 )로 구성된 문자열
() - vps

나는 어떻게 괄호 배치가 건전함을 인식하는가
() 이렇게 붙어있는 괄호를 먼저 파악한다

0 01 01 1 00 01 11
01 01 01 01 0 01 01 01 1 01

솔루션
01을 찾는다.
01을 없앤다
다시 01을 찾는다.
01을 없앤다.
문자열이 없어지면 밸리드하고
남으면 인밸리드 하다
'''



T = int(input())
for i in range(T):
    stack = []
    a = [+(i == ')') for i in input()]
    try:
        for i in range(len(a)):
            if a[i] == 0:
                stack.append(1)
            else:
                del(stack[0])

        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
    except:
        print("NO")
        


   
    #for i in range(len(a)-1):
    #    if (a[i]==0) and (a[i+1]==1):
            