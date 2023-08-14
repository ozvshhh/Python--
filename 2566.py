mtrx=[]
max_rocate = []
max_value = 0
for i in range(9):
    mtrx.append('')
for i in range(9):
    mtrx[i] = list(map(int,input().split()))


for x in range(9):
    for y in range(9):
        if mtrx[x][y] >= max_value:
            max_rocate = [x,y]
            max_value = mtrx[x][y]
        else:
            continue
        
        
print(max_value)
print(max_rocate[0]+1, max_rocate[1]+1 )
