import sys
input = sys.stdin.readline

Q = int(input())

n = 1
prod = 1
add = 0




# 0,1 명령마다 - 점화식을 재정의하고
# 2 명령마다 몇 번째(n) 수를 구할 지 설정하고
# 3 명령이 들어올 때 마다 - 점화식에 알맞은 숫자를 출력한다.


for q in range(Q):
    command = list(map(int,input().split()))
    if command[0] == 0:
        add += command[1]
    elif command[0] == 1:
        prod *= command[1]
        add *= command[1]
    elif command[0] == 2:
        n += command[1]
    elif command[0] == 3:
        print(prod*n + add)