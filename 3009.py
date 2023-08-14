sum_x = []
sum_y = []
for i in range(3):
    x,y = map(int,input().split())
    sum_x.append(x)
    sum_y.append(y)

a = 0
b = 0
for i in range(3):
    if sum_x.count(sum_x[i])%2 == 1:
        a = sum_x[i]
    if sum_y.count(sum_y[i])%2 == 1:
        b = sum_y[i]
print(a,b)