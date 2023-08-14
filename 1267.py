call_log = []

Y_bill = 0
M_bill = 0

N = int(input())

call_log = list(map(int,input().split()))

for i in range(N):
    Y_bill += (((call_log[i]//30)+1)*10)
for i in range(N):
    M_bill += (((call_log[i]//60)+1)*15)

if Y_bill == M_bill:
    print('Y M',Y_bill)
elif Y_bill < M_bill:
    print('Y',Y_bill)
elif Y_bill > M_bill:
    print('M', M_bill)
