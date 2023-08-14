#B진법 수열 N을 입력 받는다.

#예제 ZZZZZ 36 -> 60466175
#36진법에서 Z는 9 +26(알파벳개수) = 35

#1 N 값을 10진수 수열로 표현하기 *****
#2 N 값에 진수^n 값을 곱한 뒤에 더하기

N, B = input().split()
add = 0

n_digit_num = len(N)-1
    
for i in range(len(N)):
    
    if ord(N[i]) >= 65:
        add += (ord(N[i])-55)*(int(B)**n_digit_num)
    else:
        add += (int(N[i])) * (int(B)**n_digit_num)
    n_digit_num -= 1

print(add)
