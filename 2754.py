a = input()
grade = 0.0

if a[0] == 'A':
    grade += 4
elif a[0] == 'B':
    grade += 3
elif a[0] == 'C':
    grade += 2
elif a[0] == 'D':
    grade += 1
else:
    pass

if len(a) == 2:
    if a[1] == '+':
        grade += 0.3
    elif a[1] == '0':
        grade += 0.0
    elif a[1] == '-':
        grade -= 0.3
else:
    pass

print(grade)