r = 31
M = 1234567891
i = int(input())
j = input()
sum = 0
for i in range(len(j)):
    a = ((ord(j[i])-96)*(r**i))%M
    if a > M:
        sum += a - (len(j)//M)
    else:
        sum += a
print(sum)