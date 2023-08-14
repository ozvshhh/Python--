N = int(input())
numbers = str(input())
sum = 0
for i in range(N):
    sum = sum + int(numbers[-(i+1)])
print(sum)