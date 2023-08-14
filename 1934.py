import sys
input = sys.stdin.readline
LMI=lambda:list(map(int,input().split()))
II=lambda:int(input())


for i in range(II()):
    a, b = LMI()
    for i in range(a,a*b+1,a):
        if (((float(i//a))==(i/a))and(float(i//b)==(i/b))): 
            print(i)
            break