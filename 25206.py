grade_to_point = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,'C0':2.0,'D+':1.5, 'D0':1.0, 'F':0, 'P':None}
all_of_grade = 0.0
all_of_rg = 0.0
for i in range(20):
    subtitle, rate, grade = input().split()
    if grade == 'P':
        continue
    else:    
        rate = float(rate)
        all_of_rg += (grade_to_point[grade] * rate)
        all_of_grade += rate
print(all_of_rg/all_of_grade)