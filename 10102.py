V = int(input())
p = input()
#p = list(p)

if p.count('A')>p.count('B'):
    print('A')
elif p.count('A')<p.count('B'):
    print('B')
else:
    print('Tie')