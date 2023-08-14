grades = []
for i in range(5):
    a = int(input())
    if a <40:
        a = 40
    grades.append(a)
print(int(sum(grades)/len(grades)))