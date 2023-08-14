num = int(input())
sum = 1
for i in range(num):
    sum += 6*i
    if sum >= num:
        print(i+1)
        break
    else:
        pass
