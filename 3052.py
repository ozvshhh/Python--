
N_list = []
count = 0
for i in range(10):
    a = int(input())
    N_list.append(a%42)

'''
N_list.sort()

for k in range(len(N_list)-1):
    if N_list[k]==N_list[k+1]:
        continue
    else:
        count = count + 1
        '''
N_list = set(N_list)
print(N_list)
