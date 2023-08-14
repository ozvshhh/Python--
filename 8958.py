T = int(input())

for i in range(T):
    combo = 0
    point = 0
    a = input()
    for i in range(len(a)):
        if a[i] == 'O':
            combo += 1
            point += combo
        elif a[i] == 'X':
            combo = 0
    print(point)