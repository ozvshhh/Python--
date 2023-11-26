import math

T = int(input())

def lcm(a,b):
    return int(a*b/math.gcd(a,b))
    

for t in range(T):
    a,b = map(int,input().split())
    print(lcm(a,b),math.gcd(a,b))