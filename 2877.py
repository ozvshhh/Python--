'''
4와 7이 포함 된 수
n**2
2진수로 생각했을때
0일 때 4
1일 때 7
'''
a = int(input())
a_str = bin(a-1)
print(a_str)

for i in range(len(a_str)-2):
    
    if i%2 == 1:
        if (a_str[i+2]) == '0':
            print('4',end='')
        elif (a_str[i+2]) == '1':
            print('7',end='')
            
    if i%2 == 0:
        if (a_str[i+2]) == '0':
            print('7',end='')
        elif (a_str[i+2]) == '1':
            print('4',end='')
        