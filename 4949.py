while True:
        stack = []
        line = input()
        if line == ".":
            break
        for char in line:
            if char == "[":
                stack.append(0)
            if char == "]":
                if len(stack) > 0:
                    if stack[-1] == 0:
                        stack.pop()
                    else:
                        stack = [0]
                        break
                else:
                    stack = [0]
                    break
            if char == "(":
                stack.append(1)
            if char == ")":
                if len(stack) > 0:
                    if stack[-1] == 1:
                        stack.pop()
                    else:
                        stack = [0]
                        break
                
        if len(stack)%2 == 0:
            print('yes')
        else:
            print("no")
    
'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''