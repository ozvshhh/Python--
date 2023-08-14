now_h, now_m, now_s = map(int,input().split(':'))
start_h, start_m, start_s = map(int,input().split(':'))

now_whole_s = (now_h*3600) + (now_m*60)
start_whole_s = (start_h*3600) + (start_m*60)

left_whole_s = start_whole_s - now_whole_s

left_h = 0
left_m = 0
left_s = 0
for i in range(2):
    if left_whole_s//3600 > 0:
        left_h = left_whole_s//3600
        left_whole_s = left_whole_s - left_whole_s%3600
        print('h',left_h)
        print('whole',left_whole_s)
    elif left_whole_s//60 > 0:
        left_m = left_whole_s//60
        left_whole_s = left_whole_s - left_whole_s%60
        print('m',left_m)
        print('whole',left_whole_s)

        
print(f'{left_h}:{left_m}:{left_whole_s}')