music = list(map(int,input().split()))
a = 0
d = 0
for i in range(8):
    if i+1 == music[i]:
        a += 1
    elif i+1 == 9-music[i]:
        d += 1
if a == 8:
    print('ascending')
elif d == 8:
    print('descending')
else:
    print('mixed')