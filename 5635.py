T = int(input())
years = []
names = []
months = []
dates = []
for i in range(T):
    name, d, m, y = input().split()
    names.append(name)
    if len(d) == 1:
        d = '0'+d
    if len(m) == 1:
        m = '0'+m
    dates.append(int(y+m+d))
print(names[dates.index(max(dates))])
print(names[dates.index(min(dates))])
    

'''
숫자가 클 수록 나이가 어리다.
우선순위는 년 월 일 순서이다.
'''