import sys
input = sys.stdin.readline

T = int(input())

S = set({})
for t in range(T):
    command = list(input().split())
    if len(command) == 2:
        x = int(command[1])
    if command[0] == "add":
        S.add(x)
    elif command[0] == "remove":
        if x in S:
            S.remove(x)
    elif command[0] == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif command[0] == "all":
        S = set({i for i in range(1,21)})
    elif command[0] == "empty":
        S = set({})
    #print(S)