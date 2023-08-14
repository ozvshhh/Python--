a = int(input())
b = int(input())
c = int(input())
sum = a*b*c
sum = str(sum)
sum = list(map(int,sum))
for i in range(10):
    print(sum.count(i))
