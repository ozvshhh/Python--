
n = int(input())
sequence = []
for _ in range(n):
    sequence.append(int(input()))

def input(n, sequence):
    stack = []
    result = []
    now = 1
    for num in sequence:
        while now <= num:
            stack.append(now)
            result.append('+')
            now += 1
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            return ['NO']
    return result



answer = input(n, sequence)
for line in answer:
    print(line)