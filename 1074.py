import math

N,r,c = map(int,input().split())

#그냥 잘라서 범위 지정하면 될듯?
#4조각씩 존나 잘라야겠다.
#분할정복 해야겠제?
# 2*(n-1) 번 분할하기


while N != 1: 
    n = (2**N)//2
