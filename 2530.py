h,m,s = map(int,input().split())
add = int(input())

h += add//3600
add -= (add//3600)*3600


m += add//60
add -= (add//60)*60


s += add

if s >= 60:
    m += s//60
    s -= (s//60)*60
if m >= 60:
    h += m//60
    m -= (m//60)*60
if h >= 24:
    h -= (h//24)*24

print(f'{h} {m} {s}')