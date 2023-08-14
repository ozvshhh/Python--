import sys
input = sys.stdin.readline
n , money = map(int,input().split())
coins = []
count = 0

for deal in range(n):
    coins.append(int(input()))
for coin in reversed(coins):
    while coin <= money:
        count += money//coin
        money %= coin
print(count)