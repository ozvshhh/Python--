n = int(input())
a = 0
b = 0
c = 0
'''
A 300초
B 60초
C 10초
'''
if (n//10) == (n/10):
    a = n//300
    n -= 300*a
    
    b = n//60
    n -= 60*b
    
    c = n//10
    n -= 10*b
    
    print(a,b,c)
else:
    print(-1)