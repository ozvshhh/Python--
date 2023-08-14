h,m = input().split()
a = input()
h = int(h)
m = int(m)
a = int(a)

if m+(a%60) >= 60:
    m = m+(a%60) - 60
    h = h + 1
    print ('1',h,m)
else:
    m = m+(a%60)
    print ('2',h,m)
if h+(a//60) >= 24:
    h = h+(a//60)-24
    print ('3',h,m)
else:
    h = h +(a//60)
    print ('4',h,m)
