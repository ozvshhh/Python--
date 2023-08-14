import sys
input = sys.stdin.readline
LMI=lambda:list(map(int,input().split()))
II=lambda:int(input())

N = int(input())
stack = []
for i in range(N):
    commands = list(input().split())
    if len(commands) == 2:
        def_name = commands[0]
        X = int(commands[1])
    else:
        def_name = commands[0]
    
    if def_name == "push":
        stack.append(X)
    
    elif def_name == "size":
        print(len(stack))
    elif def_name == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        if def_name == "pop":
            stack.pop(-1)
        else:
            continue
            
    
    # elif def_name == "pop":
    #     if len(stack) == 0:
    #         print(-1)
    #     else:
    #         print(stack[-1])
    #         stack.remove(stack[-1])
    # elif def_name == "top":
    #     if len(stack) == 0:
    #         print(-1)
    #     else:
    #         print(stack[-1])