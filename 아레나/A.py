import sys

input = sys.stdin.readline

n = int(input())

a = (n*(n+1))//2
b = a**2
c = (n**4 + 2*(n**3) + n**2)//4

print(a)
print(b)
print(c)