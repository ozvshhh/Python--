a = float(input())

while a != 1.0:
    for i in range(2,int(a)+1,1):
        if a/i == a//i:
            print(i)
            a = a/i
            break
