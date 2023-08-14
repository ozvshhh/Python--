N = int(input())

for i in range(N):
    print(' '*(N-1-i),'*'*(i+1),end=' \n',sep='')
for i in range(N-1):
    print(' '*(i+1),'*'*(N-1-i),end=' \n',sep='')

