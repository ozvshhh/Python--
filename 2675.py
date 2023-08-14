T = int(input())

for j in range(T):
    n,k = input().split()
    n = int(n)
    
    for i in range(len(k)):
        for j in range(n):
            if i == len(k)-1:
                if j == n-1:
                    print(k[i])
                else:
                    print(k[i], end='')
            else:
                print(k[i], end='')
            