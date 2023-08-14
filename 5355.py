a = int(input())

for i in range(a):
    num = 0
    line = input().split()
    for i in range(len(line)):
        if str(line[i]) == '@':
            num *= 3
        elif str(line[i]) == '%':
            num += 5
        elif str(line[i]) == '#':
            num -= 7
        else:
            num += float(line[i])
    print(format(num,".2f"))